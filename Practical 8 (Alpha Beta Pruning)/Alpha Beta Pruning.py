
MAX_VAL = 1000
MIN_VAL = -1000

class Node():
    def __init__(self, id, val = -1):
        self.id = id
        self.val = val
        self.alpha = MIN_VAL
        self.beta = MAX_VAL
        self.next = []

    def add_next_node(self, next_nodes):
        self.next.extend(next_nodes)

    def update_alpha(self, val):
        if self.alpha < val:
            self.alpha = val

    def update_beta(self, val):
        if self.beta > val:
            self.beta = val

    def update_val(self, val, level):
        if (level == 'max' and (self.val == -1 or self.val < val)) or (level == 'min' and (self.val == -1 or self.val > val)):
            self.val = val

def create_graph():
    id_list = {'A': -1, 'B': -1, 'C': -1, 'D': 3, 'E': 5, 'F': -1, 'G': -1 , 'H': 4 , 'I': -1 , 'J': 5 , 'K': 7 , 'L': 8 , 'M': 0 , 'N': 7}
    node_list = {}
    for id in id_list:
        node_list[id] = Node(id, id_list[id])

    node_list['A'].add_next_node( [node_list['B'], node_list['C']] )
    node_list['B'].add_next_node( [node_list['D'], node_list['E']] )
    node_list['C'].add_next_node( [node_list['F'], node_list['G'], node_list['H']] )
    node_list['F'].add_next_node( [node_list['I'], node_list['J']] )
    node_list['G'].add_next_node( [node_list['K'], node_list['L']] )
    node_list['I'].add_next_node( [node_list['M'], node_list['N']] )
    
    return node_list['A']

def alpha_beta_pruning(node, level):
    print("Node Enter : " + node.id + " " + str(node.alpha) + " " + str(node.beta) + " " + str(node.val))
    if node.val != -1:
        return node.val

    next_level = 'max' if level == 'min' else 'min'

    for next_node in node.next:
        next_node.update_alpha(node.alpha)
        next_node.update_beta(node.beta)

        val = alpha_beta_pruning(next_node, next_level)
        node.update_alpha(val) if level == 'max' else node.update_beta(val)
        node.update_val(val, level)
        if node.alpha >= node.beta:
            break
    
    print("Node Exit : " + node.id + " " + str(node.alpha) + " " + str(node.beta) + " " + str(node.val))
    return node.val

if __name__ == "__main__":
    root = create_graph()
    print(alpha_beta_pruning(root, "max"))
