import heapq
from collections import deque

maze = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (0, 4)

def h(p):
    return abs(p[0] - goal[0]) + abs(p[1] - goal[1])

def bfs():
    q = deque([(start, [start])])
    visited = {start}

    while q:
        current, path = q.popleft()

        if current == goal:
            return path

        r, c = current

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            new = (nr, nc)

            if 0 <= nr < 5 and 0 <= nc < 5:
                if maze[nr][nc] == 0 and new not in visited:
                    visited.add(new)
                    q.append((new, path + [new]))

def astar():
    q = [(h(start), 0, start, [start])]
    visited = set()

    while q:
        f, cost, current, path = heapq.heappop(q)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path

        r, c = current

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            new = (nr, nc)

            if 0 <= nr < 5 and 0 <= nc < 5:
                if maze[nr][nc] == 0 and new not in visited:
                    g = cost + 1
                    heapq.heappush(q, (g + h(new), g, new, path + [new]))

bfs_path = bfs()
astar_path = astar()

print("BFS:", bfs_path)
print("A*:", astar_path)
print("BFS steps:", len(bfs_path) - 1)
print("A* steps:", len(astar_path) - 1)