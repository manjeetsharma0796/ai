from queue import PriorityQueue

class Node:
    def __init__(self, name, parent=None, cost=0, heuristic=0):
        self.name = name
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic
    
    def __lt__(self, other):
        return self.total_cost < other.total_cost

def a_star(graph, heuristics, start, goal):
    open_list = PriorityQueue()
    open_list.put(Node(start, None, 0, heuristics[start]))
    closed_list = set()

    while not open_list.empty():
        current_node = open_list.get()

        # If goal node is found, reconstruct the path
        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]  # Reverse the path to get from start to goal

        closed_list.add(current_node.name)

        for neighbor, cost in graph[current_node.name].items():
            if neighbor in closed_list:
                continue

            g_cost = current_node.cost + cost
            h_cost = heuristics[neighbor]
            total_cost = g_cost + h_cost
            open_list.put(Node(neighbor, current_node, g_cost, h_cost))
    
    return None  # Return None if no path is found

# Example graph and heuristic values
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1}
}

heuristics = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 4,
    'E': 1,
    'F': 0  # Goal node, heuristic is 0
}

start = 'A'
goal = 'F'

path = a_star(graph, heuristics, start, goal)

if path:
    print(f"Path found: {' -> '.join(path)}")
else:
    print("No path found")
