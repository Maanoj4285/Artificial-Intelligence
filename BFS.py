from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        print("Priority queue:", list(queue))  # Print current state of the queue
        vertex = queue.popleft()
        print("Visiting:", vertex)  # Print the node being visited

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


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

# Call bfs function
bfs(graph, 'S')
