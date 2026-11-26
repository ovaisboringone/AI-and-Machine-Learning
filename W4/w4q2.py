import heapq
import math

cities = {
    'A': (0, 0),
    'B': (2, 3),
    'C': (5, 2),
    'D': (6, 6),
    'E': (8, 3)
}

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

start = 'A'
goal = 'E'

def distance(a, b):
    x1, y1 = cities[a]
    x2, y2 = cities[b]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

q = [(distance(start, goal), start, [start])]
visited = set()

while q:
    h, city, path = heapq.heappop(q)

    if city in visited:
        continue

    visited.add(city)

    if city == goal:
        print(path)
        break

    for next_city in graph[city]:
        if next_city not in visited:
            heapq.heappush(
                q,
                (distance(next_city, goal), next_city, path + [next_city])
            )