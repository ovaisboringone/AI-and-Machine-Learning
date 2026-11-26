from collections import deque

maze = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
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

    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
            if maze[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
else:
    print("No path")