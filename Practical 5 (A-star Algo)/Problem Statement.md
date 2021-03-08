A * algorithm is a searching algorithm that searches for the shortest path between the initial and the final state. It is used in various applications, such as maps.

It works on heuristic, i.e. each node have a heuristic value which is an estimated value of cost to reach goal node from the current node.

A* algorithm has 3 parameters:

    g : the cost of moving from the initial cell to the current cell. Basically, it is the sum of all the cells that have been visited since leaving the first cell.

    h : also known as the heuristic value, it is the estimated cost of moving from the current cell to the final cell. The actual cost cannot be calculated until the final cell is reached. Hence, h is the estimated cost. We must make sure that there is never an over estimation of the cost.

    f : it is the sum of g and h. So, f = g + h

The way that the algorithm makes its decisions is by taking the f-value into account. The algorithm selects the smallest f-valued cell and moves to that cell. This process continues until the algorithm reaches its goal cell.

GRAPH:
Start State = S     Goal State = D

                            (S,3)
                          /      \
                       1 /        \4
                        /     2    \
                   (A,6) ---------- (B,2)
                      |  \___        |
                    12|     5\__     |2
                      |         \__  |
                   (D,0) ---------- (C,1)
                            3

