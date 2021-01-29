import random

class Node():
    def __init__(self, id):
        self.id = id
        self.next = {}

    def add_next_node(self, node, weight):
        self.next.add(node, weight)

    def get_next_state(self, id):
        for node in self.next:
            if node.id == id:
                return (node, self.next[node])

    def __eq__(self, other) -> bool:
        return self.id == other.id

def travel_cost(start_state, sequence):
    cost = 0

def get_possible_next_states(current_sequence):
    pass

def start():
    
    nodes_list = [Node(1), Node(2), Node(3), Node(4), Node(5)]

    #representation = [node1, node2, weight]
    edges_list = [[1, 2, 2], [1, 3, 3], [1, 4, 3], [1, 5, 6], [2, 3, 4], [2, 4, 5], 
                  [2, 5, 3], [3, 4, 7], [3, 5, 3], [4, 5, 3]]

    for (node1, node2, weight) in edges_list:
        nodes_list[ node1-1 ].add( nodes_list( node2-1 ), weight )
        nodes_list[ node2-1 ].add( nodes_list( node1-1 ), weight )

    node_sequence = [1, 2, 3, 4, 5]
    random.shuffle(node_sequence)


    better_neighbour_exists = True
    while better_neighbour_exists:
        better_neighbour_exists = False

        next_states = get_possible_next_states(node_sequence)
        for next_sequence in next_states:
            if travel_cost():
                pass

if __name__ == "__main__":
    start()






