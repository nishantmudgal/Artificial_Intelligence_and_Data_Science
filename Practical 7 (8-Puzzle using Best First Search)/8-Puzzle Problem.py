import copy

class State():

    visited_state = []

    def __init__(self, puzzle_state, path):
        self.path = path
        self.puzzle = puzzle_state
        self.heuristic, self.x_blank, self.y_blank = self.get_init_values()
        State.visited_state.append(hash(str(self.puzzle)))

    def get_init_values(self):
        wrong_index, x_cord, y_cord = 0, 0, 0
        goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

        for index_i in range(3):
            for index_j in range(3):
                if self.puzzle[index_i][index_j] != goal_state[index_i][index_j]:
                    wrong_index += 1
                if self.puzzle[index_i][index_j] == 0:
                    x_cord = index_i
                    y_cord = index_j

        return wrong_index, x_cord, y_cord

    def is_goal_state(self):
        return self.heuristic == 0

    def get_next_states(self):
        next_states = []

        if (self.x_blank - 1) >= 0:
            new_state = copy.deepcopy(self.puzzle)
            new_state[self.x_blank][self.y_blank] = new_state[self.x_blank-1][self.y_blank]
            new_state[self.x_blank-1][self.y_blank] = 0
            if hash(str(new_state)) not in State.visited_state:
                next_states.append(State(new_state, self.path + " -> \n" + str(new_state)))

        if (self.x_blank + 1) <= 2:
            new_state = copy.deepcopy(self.puzzle)
            new_state[self.x_blank][self.y_blank] = new_state[self.x_blank+1][self.y_blank]
            new_state[self.x_blank+1][self.y_blank] = 0
            if hash(str(new_state)) not in State.visited_state:
                next_states.append(State(new_state, self.path + " -> \n" + str(new_state)))

        if (self.y_blank - 1) >= 0:
            new_state = copy.deepcopy(self.puzzle)
            new_state[self.x_blank][self.y_blank] = new_state[self.x_blank][self.y_blank-1]
            new_state[self.x_blank][self.y_blank-1] = 0
            if hash(str(new_state)) not in State.visited_state:
                next_states.append(State(new_state, self.path + " -> \n" + str(new_state)))

        if (self.y_blank + 1) <= 2:
            new_state = copy.deepcopy(self.puzzle)
            new_state[self.x_blank][self.y_blank] = new_state[self.x_blank][self.y_blank+1]
            new_state[self.x_blank][self.y_blank+1] = 0
            if hash(str(new_state)) not in State.visited_state:
                next_states.append(State(new_state, self.path + " -> \n" + str(new_state)))

        return next_states

def best_first_search(state):
    queue = [state]
    heuristic_lambda = lambda x : x.heuristic
    itr = 0
    while len(queue) > 0 and itr < 100:
        current_state = queue[0]
        queue = queue[1:]
        if current_state.is_goal_state():
            return current_state.path
        next_states = current_state.get_next_states()
        queue.extend(next_states)
        queue = sorted(queue, key = heuristic_lambda)
        itr += 1

if __name__ == "__main__":
    initial_state = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
    print(best_first_search(State(initial_state, str(initial_state))))
