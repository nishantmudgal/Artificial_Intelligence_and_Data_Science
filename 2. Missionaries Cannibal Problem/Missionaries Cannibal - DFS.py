'''
Missionary Cannibal Problem - Implemented using DFS

In this problem, three missionaries and three cannibals must cross a river using a boat which can carry 
at most two people, under the constraint that, for both banks, that the missionaries present on the bank 
cannot be outnumbered by cannibals. The boat cannot cross the river by itself with no people on board. 

NISHANT MUDGAL
M.tech (IT)
NSUT

'''
# list of possible moves
possible_operations = [[1,0], [0,1], [1,1], [2,0], [0,2]]

# this set to keep track of all the visited states
visited_states = set()


class State():
    
    def __init__(self, cannibals, missionaries, boat):
        self.cannibals = cannibals
        self.missionaries = missionaries
        self.boat = boat
        self.next = []

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
        
    # Return hash of the current state useful for making the class hashable
    def __hash__(self):
        return hash((self.cannibals, self.missionaries, self.boat))

    # Function to equate 2 State objects with one another
    def __eq__(self, other):
        return self.cannibals == other.cannibals and self.missionaries == other.missionaries and self.boat == other.boat

    #define string representation of the class
    def __str__(self):
        return "( " + str(self.cannibals) + ", " + str(self.missionaries) + ", " + str(self.boat)+ " )"


#Returns list of all the possible next state
def possible_paths(state):

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

        # Checks if the state is already visited or not
        if next_state not in visited_states:
            visited_states.add(next_state)
            possible_next_state.append(next_state)

    return possible_next_state

#Implementation of DFS function
def dfs(root):
    
    #Return True if the goal state is reached
    if root.is_goal_state():
        return True

    #Return False if the current state is not valid
    if not root.is_valid_state():
        return False

    #gets all the possible next state from the current state
    next_states = possible_paths(root)
    
    #variable to keep track, if the current state state have any path to the goal state
    have_path = False
    
    #Apply DFS to all the possible next state
    for state in next_states:
        if dfs(state):
            root.next.append(state)
            have_path = True

    #Returns True if the goal state can be reached from the current state
    return have_path

#Function to print all the possible paths from start state to goal state
def print_possible_path(state):

    print("\nRepresentation = ( Number of Cannibals, Number of Missionaries, Position of the Boat )")
    print("Start State = ( 3, 3, 1) \nGoal State = ( 0, 0, 0)\n")

    print("Path:")
    while not state.is_goal_state():
        print(state , end = " -> ")
        state = state.next[0]

    print(state, end = '\n\n')

#Main function to set initial state and start DFS on the problem to find all the possible paths
def start_game():

    #Set initial state and add it to the visited state
    initial_state = State(3, 3, 1)
    visited_states.add(initial_state)
    
    #Run DFS
    have_path = dfs(initial_state)

    #to print path the it exists from initial state to final
    if have_path:
        print_possible_path(initial_state)
    else:
        print("No path found from Start State to Goal State")

#Check for main function
if __name__ == '__main__':
    start_game()