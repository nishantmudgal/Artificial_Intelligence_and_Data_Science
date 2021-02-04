'''
The travelling salesman problem (also called the  TSP) asks the following question:

Given a list of cities and the distances between each pair of cities, what is the shortest possible
 route that visits each city exactly once and returns to the origin city?

Goal is to implement the solution of the TSP using Hill Climbing Algorithm.

-Nishant Mudgal
'''
import random

class Node():
    def __init__(self, id):
        self.id = id
        self.next = {}

    def add_next_node(self, node, weight):
        self.next[str(node.id)] = [node, weight]
        node.next[str(self.id)] = [self, weight]

    def get_next_state(self, id):
        if id == self.id:
            return [self]

        return self.next[str(id)]

    def __eq__(self, other) -> bool:
        return self.id == other.id

def travel_cost(start_state, sequence):
    cost = 0
    current_state = start_state
    
    for node_id in sequence[1:]:
        next_state = current_state.get_next_state(node_id)
        cost = cost + next_state[1]
        current_state = next_state[0]

    return cost

def generate_next_sequence(current_sequence):
    length_sequence = len(current_sequence)
    i = 0
    j = 1
    while i < length_sequence-1:

        next_sequence = current_sequence
        next_sequence[i], next_sequence[j] = next_sequence[j], next_sequence[i]

        yield next_sequence

        if j == length_sequence-1:
            i = i+1
            j = i+1
        else:
            j = j+1


def create_graph():
    
    #Creating Nodes
    start_node = Node('1')
    node_2 = Node('2')
    node_3 = Node('3')
    node_4 = Node('4')
    node_5 = Node('5')

    #Adding edges
    start_node.add_next_node(node_2, 2)
    start_node.add_next_node(node_3, 3)
    start_node.add_next_node(node_4, 3)
    start_node.add_next_node(node_5, 6)

    node_2.add_next_node(node_3, 4)
    node_2.add_next_node(node_4, 5)
    node_2.add_next_node(node_5, 3)

    node_3.add_next_node(node_4, 7)
    node_3.add_next_node(node_5, 3)

    node_4.add_next_node(node_5, 3)

    return start_node

def start():
    
    start_node = create_graph()

    node_sequence = ['1', '2', '3', '4', '5']
    random.shuffle(node_sequence)

    first_node = start_node.get_next_state(node_sequence[0])[0]
    min_cost = travel_cost( first_node, node_sequence )
  
    print("\nRepresentation : [SEQUENCE][TRAVEL COST]\nPath:", end='\n')
    print(str(node_sequence) + '[' + str(min_cost) + ']', end='' )

    better_neighbour_exists = True
    while better_neighbour_exists:
        better_neighbour_exists = False

        next_states = generate_next_sequence(node_sequence)
        for next_sequence in next_states:

            first_node = start_node.get_next_state(next_sequence[0])[0]
            current_cost = travel_cost(first_node, next_sequence)

            if current_cost < min_cost:

                min_cost = current_cost
                better_neighbour_exists = True
                node_sequence = next_sequence
                print("  ->  " + str(node_sequence) + '[' + str(current_cost) + ']', end='' )
                break

if __name__ == "__main__":
    start()






