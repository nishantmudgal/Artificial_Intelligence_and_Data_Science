'''
Missionary Cannibal Problem - Implemented using BFS

In this problem, three missionaries and three cannibals must cross a river using a boat which can carry 
at most two people, under the constraint that, for both banks, that the missionaries present on the bank 
cannot be outnumbered by cannibals. The boat cannot cross the river by itself with no people on board. 

NISHANT MUDGAL
M.tech (IT)
NSUT

'''

possible_operations = [[1,1], [2,0], [0,2], [1,0], [0,1]]

class State():

    def __init__(self, cannibals, missionaries, boat):
        self.cannibals = cannibals
        self.missionaries = missionaries
        self.boat = boat
        self.prev = None
        
    #Returns True if the current state is the goal state
    def is_goal_state(self):
        return self.cannibals == 0 and self.missionaries == 0 and self.boat == 0

    #Returns True if the current state is a valid state i.e. no of cannibals is less than missionaries on both side
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
    
    #define string representation of the class
    def __str__(self):
        return "( " + str(self.cannibals) + ", " + str(self.missionaries) + ", " + str(self.boat)+ " )"


def possible_next_moves(state):
    possible_next_state = []

    # Contains no of missionaries/cannibals on the side of boat
    no_of_cannibals = state.cannibals
    no_of_missionaries = state.missionaries

    if state.boat == 0:
        no_of_cannibals = 3 - no_of_cannibals
        no_of_missionaries = 3 - no_of_missionaries

    #Goes through list of all the possible moves and adds the valid next state to variable 'possible_next_state'
    for operation in possible_operations:

        #if the moves can't be made due to insufficient number of missionaries/cannibals
        if no_of_cannibals < operation[0] or no_of_missionaries < operation[1]:
            continue
        
        #Creates next state based on boat possition
        if state.boat == 0:
            next_state = State( state.cannibals + operation[0], state.missionaries + operation[1], 1 )
        else:
            next_state = State( state.cannibals - operation[0], state.missionaries - operation[1], 0 )

        if next_state.is_valid_state():
            possible_next_state.append(next_state)

    return possible_next_state


def BFS(state):
    unique_states = set()
    unique_states.add(state)

    queue = [state]

    while len(queue) != 0:
        current_state = queue.pop()
        possible_states = possible_next_moves(current_state)
        
        for next_state in possible_states:
            
            if next_state not in unique_states:
                unique_states.add(next_state)
                queue.append(next_state)




def start_game():
    initial_state = State(3,3,1)

    BFS(initial_state)


    



if __name__ == "__main__":
    start_game()

