
class Node():

    def __init__(self, id, heuristic) -> None:
        self.id = id
        self.heuristic = heuristic
        self.distance_from_start = 0
        self.path = 'S'
        self.next = {}

    def add_next_node(self, node, weight):
        self.next[str(node.id)] = [node, weight]

    def show_result(self):
        return "Path : " + self.path + "\nCost : " + str(self.distance_from_start)

    def get_estimated_distance(self):
        return self.distance_from_start + self.heuristic

    def __repr__(self) -> str:
        return str(self.id) + " " + str(self.heuristic)
    def __eq__(self, o: object) -> bool:
        return self.id == o.id

    def __hash__(self) -> int:
        return hash(self.id, self.heuristic)

    def isGoalNode(self):
        return self.heuristic == 0

def create_graph():
    #create nodes
    start_node = Node('S', 3)
    node_a = Node('A', 6)
    node_b = Node('B', 2)
    node_c = Node('C', 1)
    node_d = Node('D', 0)

    #add edges
    start_node.add_next_node(node_a, 1)
    start_node.add_next_node(node_b, 4)
    node_a.add_next_node(node_b, 2)
    node_a.add_next_node(node_c, 5)
    node_a.add_next_node(node_d, 12)
    node_b.add_next_node(node_c, 2)
    node_c.add_next_node(node_d, 3)

    return start_node

def implementAStar(node):
    #[node, distance from start, path]
    queue = [node]

    while len(queue) > 0:
        current_node = queue[0]
        queue = queue[1:]

        if current_node.isGoalNode():
            return current_node

        for next_node in current_node.next.values():
            
            if next_node[0].distance_from_start == 0 or next_node[0].distance_from_start > current_node.distance_from_start + next_node[1]:
                if next_node[0] in queue:
                    queue.remove(next_node[0])
                
                next_node[0].distance_from_start = current_node.distance_from_start + next_node[1]
                next_node[0].path = str(current_node.path) + " -> " + str(next_node[0].id)

            index = 0
            while index < len(queue) and queue[index].get_estimated_distance() < next_node[0].get_estimated_distance() :
                    index = index + 1

            queue.insert(index, next_node[0])

    return None

def main():

    start_node = create_graph()
    goal_node = implementAStar(start_node)
    print("{}".format(goal_node.show_result()))

if __name__ == "__main__":
    main()