from collections import deque
maze =[[0,0,0],
       [0,1,0],
       [0,0,0]]
start =(2,0)
end =(0,2)

queue=deque([(start, [start])])
visited ={start}

while queue:
    (r,c),path=queue.popleft()
    
    if (r,c)==end:
        print(path)
        break


nr = r-1
nc=c

if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
    if maze[nr][nc] == 0 and (nr, nc) not in visited:
        visited.add((nr, nc))
        queue.append(((nr, nc), path + [(nr, nc)]))

    
nr =r+1
nc=c
if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
    if maze[nr][nc] == 0 and (nr, nc) not in visited:
        visited.add((nr, nc))
        queue.append(((nr, nc), path + [(nr, nc)]))

nr=r
nc=c-1
if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
    if maze[nr][nc] == 0 and (nr, nc) not in visited:
        visited.add((nr, nc))
        queue.append(((nr, nc), path + [(nr, nc)]))
        
nr=r
nc=c+1
if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
    if maze[nr][nc] == 0 and (nr, nc) not in visited:
        visited.add((nr, nc))
        queue.append(((nr, nc), path + [(nr, nc)]))
        
else:
    print("No path")