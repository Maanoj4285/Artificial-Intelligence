import math

# Function to find the minimum cost of the Travelling Salesman Problem
def tsp(graph, pos, visited, memo):
    if visited == (1 << len(graph)) - 1:
        return graph[pos][0]
    
    if memo[pos][visited] is not None:
        return memo[pos][visited]
    
    min_cost = float('inf')
    
    for city in range(len(graph)):
        if visited & (1 << city) == 0:
            new_visited = visited | (1 << city)
            cost = graph[pos][city] + tsp(graph, city, new_visited, memo)
            min_cost = min(min_cost, cost)
    
    memo[pos][visited] = min_cost
    return min_cost

def find_min_cost_tsp(graph):
    n = len(graph)
    memo = [[None] * (1 << n) for _ in range(n)]
    return tsp(graph, 0, 1, memo)

# Example graph as an adjacency matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_cost = find_min_cost_tsp(graph)
print(f"The minimum cost of the Travelling Salesman Problem is: {min_cost}")
