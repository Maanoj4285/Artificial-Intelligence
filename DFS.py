def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(f"Visited: {vertex}, Stack: {stack}")

            # Push neighbors onto the stack in reverse order (to maintain DFS order)
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
                    print(f"Pushed: {neighbor}, Stack: {stack}")


# Example graph represented as an adjacency list
graph = {
    'S': ['A', 'B', 'C'],
    'A': ['D'],
    'D': ['G'],
    'B': ['E'],
    'E': ['G'],
    'C': ['F'],
    'F': ['G'],
    'G': ['D', 'E', 'F']
}

# Call dfs function
print("DFS traversal starting from node 'A' with stack formation:")
dfs(graph, 'S')
