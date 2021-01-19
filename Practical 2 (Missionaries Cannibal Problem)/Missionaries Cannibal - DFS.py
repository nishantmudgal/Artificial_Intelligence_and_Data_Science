
possible_operations = [[1,0], [0,1], [1,1], [2,0], [0,2]]
visited_states = set()


class State():
    
    def __init__(self, cannibals, missionaries, boat):
        self.cannibals = cannibals
        self.missionaries = missionaries
        self.boat = boat
        self.next = []

    def is_goal_state(self):
        return self.cannibals == 0 and self.missionaries == 0 and self.boat == 0

    def is_valid_state(self):
        if self.missionaries != 0 and self.cannibals != 0 and self.missionaries < self.cannibals :
            return False
        elif 3 - self.missionaries != 0 and 3 - self.cannibals != 0 and 3 - self.missionaries < 3 - self.cannibals :
            return False
        else:
            return True
        
    def __hash__(self):
        return hash((self.cannibals, self.missionaries, self.boat))

    def __eq__(self, other):
        return self.cannibals == other.cannibals and self.missionaries == other.missionaries and self.boat == other.boat


def possible_paths(state):

    possible_next_state = []

    no_of_cannibals = state.cannibals
    no_of_missionaries = state.missionaries

    if state.boat == 0:
        no_of_cannibals = 3 - no_of_cannibals
        no_of_missionaries = 3 - no_of_missionaries

    for operation in possible_operations:
        if no_of_cannibals < operation[0] or no_of_missionaries < operation[1]:
            continue
        
        if state.boat == 0:
            next_state = State( state.cannibals + operation[0], state.missionaries + operation[1], 1 )
        else:
            next_state = State( state.cannibals - operation[0], state.missionaries - operation[1], 0 )

        if next_state not in visited_states:
            visited_states.add(next_state)
            possible_next_state.append(next_state)

    return possible_next_state

def dfs(root):
    
    if root.is_goal_state():
        return True

    if not root.is_valid_state():
        return False

    have_path = False
    next_states = possible_paths(root)
    
    for state in next_states:
        if dfs(state):
            root.next.append(state)
            have_path = True

    return have_path


def print_possible_path(state):
    current_state = state
    while(len(current_state.next) != 0):
        print(str(current_state.cannibals) + " " + str(current_state.missionaries) )
        current_state = current_state.next[0]
    
    print(str(current_state.cannibals) + " " + str(current_state.missionaries) )
    

def start_game():
    initial_state = State(3, 3, 1)
    visited_states.add(initial_state)
    have_path = dfs(initial_state)

    if have_path:
        print_possible_path(initial_state)
    else:
        print("No path found from Start State to Goal State")

if __name__ == '__main__':
    start_game()