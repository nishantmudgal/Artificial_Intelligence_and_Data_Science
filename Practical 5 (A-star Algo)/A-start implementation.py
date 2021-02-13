'''
A * algorithm is a searching algorithm that searches for the shortest path between the initial and 
the final state. It is used in various applications, such as maps.
It works on heuristic, i.e. each node have a heuristic value which is an estimated value of cost to 
reach goal node from the current node.
Goal is to find the path from Start Node to Goal Node with minimum cost.

Nishant Mudgal
'''
class Node():

    def __init__(self, id, heuristic) -> None:
        self.id = id
        self.heuristic = heuristic
        self.distance_from_start = 0
        self.path = 'S'
        self.next = {}

    # Add next nodes
    def add_next_node(self, node, weight):
        self.next[str(node.id)] = [node, weight]

    # Return path and cost from start node to current node
    def show_result(self):
        return "Path : " + self.path + "\nCost : " + str(self.distance_from_start)

    # Return estimated distance from start node to goal node via current node
    def get_estimated_distance(self):
        return self.distance_from_start + self.heuristic

    # To equate two Node objects
    def __eq__(self, o: object) -> bool:
        return self.id == o.id

    # Return True if current node is goal node
    def isGoalNode(self):
        return self.heuristic == 0

# Create the complete graph and return the start node
def create_graph():
    # Create nodes
    start_node = Node('S', 3)
    node_a = Node('A', 6)
    node_b = Node('B', 2)
    node_c = Node('C', 1)
    node_d = Node('D', 0)

    # Add edges
    start_node.add_next_node(node_a, 1)
    start_node.add_next_node(node_b, 4)
    node_a.add_next_node(node_b, 2)
    node_a.add_next_node(node_c, 5)
    node_a.add_next_node(node_d, 12)
    node_b.add_next_node(node_c, 2)
    node_c.add_next_node(node_d, 3)

    return start_node

def implementAStar(node):

    queue = [node]

    while len(queue) > 0:

        # Remove first element of the queue and add the next nodes in sorting order in the queue
        current_node = queue[0]
        queue = queue[1:]

        if current_node.isGoalNode():
            return current_node

        for next_node in current_node.next.values():
            # If this node is not explored yet or the previous distance from start to here was more
            if next_node[0].distance_from_start == 0 or next_node[0].distance_from_start > current_node.distance_from_start + next_node[1]:
                if next_node[0] in queue:
                    queue.remove(next_node[0])
                
                next_node[0].distance_from_start = current_node.distance_from_start + next_node[1]
                next_node[0].path = str(current_node.path) + " -> " + str(next_node[0].id)

            # Find the index at which the next node should be added such that the queue remains in sorted order
            index = 0
            while index < len(queue) and queue[index].get_estimated_distance() < next_node[0].get_estimated_distance() :
                    index = index + 1

            queue.insert(index, next_node[0])

    return None

def main():

    # Get Start Node and create graph
    start_node = create_graph()

    # Find the shortest path from start to goal node using a* algorithm
    goal_node = implementAStar(start_node)

    # Print path and cost from start to goal node
    print(goal_node.show_result())

if __name__ == "__main__":
    main()