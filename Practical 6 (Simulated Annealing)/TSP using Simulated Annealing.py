import random
import math

def get_function(initial_state):

    weight_matrix = [ [0, 2, 3, 3, 6],
                      [2, 0, 4, 5, 3],
                      [3, 4, 0, 7, 3],
                      [4, 5, 7, 0, 3],
                      [6, 3, 3, 3, 0], ]
    visited_states = []

    def get_cost(state):
        cost = 0
        for index in range(len(state)-1):
            cost = cost + weight_matrix[state[index]-1][state[index+1]-1]

        return cost
        
    def get_neighbors(state):

        length_state = len(state)
        i = random.randint(0, length_state-1)
        j = random.randint(0, length_state-1)
        hash_value = 0
        next_state = [*state]
        next_state[i], next_state[j] = next_state[j], next_state[i]
        hash_value = hash(str(next_state))
        while i == j or hash_value in visited_states:
            
            i = random.randint(0, length_state-1)
            j = random.randint(0, length_state-1)
            if i == j:
                continue

            next_state[i], next_state[j] = next_state[j], next_state[i]
            hash_value = hash(str(next_state))

        visited_states.append(hash_value)
        return next_state

    def print_state(state, first_print):
        if first_print:
            print("State Path:")
        else:
            print(" -> ", end = "")

        print((state, get_cost(state)), end="")

    visited_states.append(hash(str(initial_state)))
    return get_cost, get_neighbors, print_state


def simulated_annealing(initial_state):

    func_get_cost, func_get_neighbour, func_print_state = get_function(initial_state)

    initial_temp = 150
    final_temp = 0
    alpha = 10
    
    current_temp = initial_temp

    current_state = initial_state
    solution = current_state
    func_print_state(current_state, True)

    while current_temp > final_temp:
        
        func_print_state(current_state, False)
        neighbor = func_get_neighbour(current_state)

        cost_diff = func_get_cost(current_state) - func_get_cost(neighbor)

        if cost_diff > 0:
            current_state = neighbor
        else:
            if random.uniform(0, 1) < math.exp(-cost_diff / current_temp):
                current_state = neighbor


        if func_get_cost(current_state) < func_get_cost(solution):
            solution = current_state
        current_temp -= alpha

    return solution, func_get_cost(solution)
    
def main():

    initial_state = [1,2,3,4,5]
    random.shuffle(initial_state)

    print("\n\nFinal Solution : " + str(simulated_annealing(initial_state)))

if __name__ == "__main__":
    main()