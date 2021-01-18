
possible_operations = [(1,0), (0,1), (1,1), (2,0), (0,2)]


class State():
    
    def __init__(self, cannibals, missionaries, boat):
        self.cannibals = cannibals
        self.missionaries = missionaries
        self.boat = boat
        self.next = []

    def is_goal_state(self):
        return self.cannibals == 0 and self.missionaries == 0 and self.boat == 0

    def __hash__(self):
        return hash((self.cannibals, self.missionaries, self.boat))

    def __eq__(self, other):
        return self.cannibals == other.cannibal and self.missionaries == other.missionaries and self.boat == other.boat


def possible_paths(state):

    possible_next_state = []

    for operation in possible_operations:
        pass

    return possible_next_state

def dfs(root):
    
    if root.is_goal_state():
        return True

    have_path = False
    next_states = possible_paths(root)
    
    for state in next_states:
        if dfs(state):
            root.next.append(state)
            have_path = True

    return have_path


def print_possible_path(state):
    pass

def start_game():
    initial_state = State(3, 3, 1)
    
    have_path = dfs(initial_state)

    if have_path:
        print_possible_path(initial_state)
    else:
        print("No path found from Start State to Goal State")

if __name__ == '__main__':
    start_game()