import math
import heapq

cities = {
    'A': (0, 0),
    'B': (2, 3),
    'C': (5, 2),
    'D': (6, 6),
    'E': (8, 3)
}

def dist(a, b):
    x1, y1 = cities[a]
    x2, y2 = cities[b]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def mst_cost(nodes):
    if len(nodes) <= 1:
        return 0

    used = {nodes[0]}
    cost = 0

    while len(used) < len(nodes):
        best = float('inf')

        for a in used:
            for b in nodes:
                if b not in used:
                    best = min(best, dist(a, b))

        cost += best

        for b in nodes:
            if b not in used:
                if any(abs(dist(a, b) - best) < 1e-9 for a in used):
                    used.add(b)
                    break

    return cost

start = 'A'
q = [(0, 0, start, {start}, [start])]

while q:
    f, cost, current, visited, path = heapq.heappop(q)

    if len(visited) == len(cities):
        cost += dist(current, start)
        print("Path:", path + [start])
        print("Cost:", round(cost, 2))
        break

    for city in cities:
        if city not in visited:
            new_cost = cost + dist(current, city)
            remaining = [x for x in cities if x not in visited and x != city]
            h = mst_cost(remaining)

            heapq.heappush(
                q,
                (new_cost + h, new_cost, city, visited | {city}, path + [city])
            )