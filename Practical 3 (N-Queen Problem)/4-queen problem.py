import copy

class State():

    def __init__(self, position_q1, position_q2, position_q3, position_q4):
        self.position_q1 = position_q1
        self.position_q2 = position_q2
        self.position_q3 = position_q3
        self.position_q4 = position_q4
        self.next = []

    def is_valid_state(self):

        if ( self.position_q1 == self.position_q2 or abs(self.position_q1 - self.position_q2) == 1 ) and self.position_q2 != -1:
            return False
        if ( self.position_q1 == self.position_q3 or abs(self.position_q1 - self.position_q3) == 2 ) and self.position_q3 != -1:
            return False
        if ( self.position_q1 == self.position_q4 or abs(self.position_q1 - self.position_q4) == 3 ) and self.position_q4 != -1:
            return False
        if ( self.position_q2 == self.position_q3 or abs(self.position_q2 - self.position_q3) == 1 ) and self.position_q3 != -1:
            return False
        if ( self.position_q2 == self.position_q4 or abs(self.position_q2 - self.position_q4) == 2 ) and self.position_q4 != -1:
            return False
        if ( self.position_q3 == self.position_q4 or abs(self.position_q3 - self.position_q4) == 1 ) and self.position_q4 != -1:
            return False

        return True

    def valid_column(self):

        col_list = [0, 1, 2, 3]

        if self.position_q1 in col_list:
            col_list.remove(self.position_q1)
        if self.position_q2 in col_list:
            col_list.remove(self.position_q2)
        if self.position_q3 in col_list:
            col_list.remove(self.position_q3)
        if self.position_q4 in col_list:
            col_list.remove(self.position_q4)

        return col_list

    def set_position(self, queen_number, position):

        if queen_number == 1:
            self.position_q1 = position
        elif queen_number == 2:
            self.position_q2 = position
        elif queen_number == 3:
            self.position_q3 = position
        elif queen_number == 4:
            self.position_q4 = position
        else:
            print("Invalid Argument passed to set_coordinated function " + queen_number)

    def __str__(self):
        return ('(' + str(self.position_q1) + ", " + str(self.position_q2) + ", " + 
                 str(self.position_q3) + ", " + str(self.position_q4) + ")")

def DFS(state, queen_number):

    if queen_number == 5:
        return state.is_valid_state()

    if  not state.is_valid_state():
        return False

    valid_column_list = state.valid_column()

    path_found = False

    for next_column in valid_column_list:
        next_state = copy.deepcopy(state)
        next_state.set_position(queen_number, next_column)

        if DFS(next_state, queen_number + 1):
            state.next.append(next_state)
            path_found = True

    return path_found


def printAllPaths(state):

    current_path = []

    def path_dfs(current_state):

        current_path.append(current_state)
        
        if len(current_state.next) == 0:
            
            print("Path :")
            print(*current_path, sep=" -> ", end="\n\n")
    
            if len(current_path) != 0:
                current_path.pop()
            return

        for next in current_state.next:
            path_dfs(next)
            
            if len(current_path) != 0:
                current_path.pop()

    path_dfs(state)


def main():
    start_state = State(-1, -1, -1, -1)
    
    DFS(start_state, 1)

    printAllPaths(start_state)

if __name__ == "__main__":
    main()





