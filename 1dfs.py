def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'F'],
    'B': ['D', 'E'],
    'F': ['C'],
    'C': [],
    'D': [],
    'E': []
}

visited_nodes = dfs(graph, 'A')
print("Visited nodes:", visited_nodes)