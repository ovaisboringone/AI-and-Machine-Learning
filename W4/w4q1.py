import heapq

grid = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 0]
]

start = (0, 0)
goal = (3, 3)

def h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

q = [(h(start, goal), 0, start, [start])]
visited = set()

while q:
    f, cost, current, path = heapq.heappop(q)

    if current in visited:
        continue

    visited.add(current)

    if current == goal:
        print(path)
        break

    r, c = current

    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0:
            new = (nr, nc)

            if new not in visited:
                g = cost + 1
                heapq.heappush(q, (g + h(new, goal), g, new, path + [new]))