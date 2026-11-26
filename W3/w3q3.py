from collections import deque

grid = [
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 0]
]

start = (0, 0)
goal = (3, 3)

queue = deque([(start, [start])])
visited = {start}

while queue:
    (r, c), path = queue.popleft()

    if (r, c) == goal:
        print(path)
        break

    for dr, dc in [(0, 1), (1, 0)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            if grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
else:
    print("No path")