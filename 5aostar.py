class AONode:
    def __init__(self, name, cost=0, is_or_node=True):
        # Initialize node with name, cost, and the type of node (OR by default)
        self.name = name
        self.cost = cost
        self.children = []
        self.solution = False
        self.is_or_node = is_or_node  # True if it's an OR node, False if it's an AND node

    def add_child(self, children):
        self.children.append(children)

def ao_star(node):
    if node.solution:
        return node.cost

    if not node.children:
        return node.cost

    if node.is_or_node:  # OR node: take the minimum cost over children
        min_cost = float('inf')
        for child_set in node.children:
            cost = 0
            for child in child_set:
                cost += ao_star(child)
            min_cost = min(min_cost, cost)
        node.cost = min_cost
        node.solution = True
    else:  # AND node: sum the costs of all children
        total_cost = 0
        for child_set in node.children:
            cost = 0
            for child in child_set:
                cost += ao_star(child)
            total_cost += cost
        node.cost = total_cost
        node.solution = True
    
    return node.cost

# Example of using AO* algorithm on an And-Or tree
A = AONode("A", is_or_node=True)
B = AONode("B", 5, is_or_node=False)
C = AONode("C", 2, is_or_node=False)
D = AONode("D", 3, is_or_node=True)
E = AONode("E", 6, is_or_node=False)

A.add_child([B, C])  # OR node A, children are B and C (OR node, choose the minimum cost)
A.add_child([D])     # OR node A, child D (AND node)
C.add_child([E])     # AND node C, child E (must both be solved)

# Calculate minimum cost to solve from the root node (A)
print("Minimum cost to solve:", ao_star(A))
