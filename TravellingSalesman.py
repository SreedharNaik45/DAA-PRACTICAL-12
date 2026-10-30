from itertools import permutations
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
n = len(graph)
def tsp(graph):
    cities = list(range(n))
    start = 0
    remaining = cities[1:]
    min_cost = float('inf')
    best_path = []
    for path in permutations(remaining):
        route = (start,) + path + (start,)
        cost = 0
        for i in range(len(route) - 1):
            cost += graph[route[i]][route[i + 1]]
        if cost < min_cost:
            min_cost = cost
            best_path = route
    print("Best Route:", " -> ".join(map(str, best_path)))
    print("Minimum Cost:", min_cost)
tsp(graph)
