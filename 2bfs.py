from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])  # Store the path to track the shortest path
    visited.add(start)
    
    while queue:
        vertex, path = queue.popleft()
        if vertex == goal:
            return path
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

path = bfs(graph, 'A', 'F')
print("Shortest path:", path)