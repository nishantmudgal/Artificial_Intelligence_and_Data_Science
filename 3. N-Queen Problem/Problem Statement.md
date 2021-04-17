The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.

Queens can attack each other if they are in same row, column or diagonal.
Goal is to find all the possible states where no 2 queens can attack each other.
This problem can be solves by using DFS or BFS. Here we have used DFS to solve this problem.

Each queen is in different rows and column number is represented using (1, 2, 3, 4). And '-1' is used to show that the corresponding queen is not set on the board.

Each state is represented by the following representation:
(Column number of q1, Column number of q2, Column number of q3, Column number of q4)

Output = All the paths through any of the goal state can be reached