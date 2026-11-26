import heapq

grid = [
    [1, 1, 5, 1, 1],
    [1, 9, 5, 9, 1],
    [1, 1, 1, 1, 1],
    [9, 5, 9, 5, 1],
    [1, 1, 1, 1, 1]
]

start = (0, 0)
goal = (4, 4)

def h(p):
    return abs(p[0] - goal[0]) + abs(p[1] - goal[1])

q = [(h(start), 0, start, [start])]
visited = set()

while q:
    f, cost, current, path = heapq.heappop(q)

    if current in visited:
        continue

    visited.add(current)

    if current == goal:
        print("Path:", path)
        print("Cost:", cost)
        break

    r, c = current

    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            if grid[nr][nc] != 9:
                new = (nr, nc)
                new_cost = cost + grid[nr][nc]

                if new not in visited:
                    heapq.heappush(
                        q,
                        (new_cost + h(new), new_cost, new, path + [new])
                    )