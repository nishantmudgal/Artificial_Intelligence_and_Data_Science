
valid_moves = [[1,1], [2,0], [0,2], [1,0], [0,1]]

class State():
    cannibals = -1
    missionaries = -1
    boat = -1

    def __init__(self, cannibals, missionaries, boat):
        self.cannibals = cannibals
        self.missionaries = missionaries
        self.boat = boat

    def __hash__(self):
        return hash((self.cannibals, self.missionaries, self.boat))

    def __eq__(self, other):
        return self.cannibals == other.cannibals and self.missionaries == other.missionaries and self.boat == other.boat

def start_game():
    path = set()
    initial_state = State(3,3,1)

    



if __name__ == "__main__":
    start_game()

