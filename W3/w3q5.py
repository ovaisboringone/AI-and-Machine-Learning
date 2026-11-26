from collections import deque

def safe(state):
    f, x, c, g = state

    if x == c and f != x:
        return False
    if c == g and f != c:
        return False

    return True

start = (0, 0, 0, 0)
goal = (1, 1, 1, 1)

q = deque([(start, [start])])
visited = {start}

while q:
    state, path = q.popleft()

    if state == goal:
        for s in path:
            print(s)
        break

    f, x, c, g = state
    moves = []

    moves.append((1-f, x, c, g))
    moves.append((1-f, 1-x, c, g))
    moves.append((1-f, x, 1-c, g))
    moves.append((1-f, x, c, 1-g))

    for new in moves:
        if safe(new) and new not in visited:
            visited.add(new)
            q.append((new, path + [new]))