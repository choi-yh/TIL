from collections import deque

def bfs(grid, start, end):
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    dist = [[0] * len(grid[0]) for _ in range(len(grid))]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append((start[0], start[1]))
    visited[start[0]][start[1]] = True
    while q:
        x, y = q.popleft()
        
        if (x, y) == end:
            return dist[x][y]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < len(grid)
                and 0 <= ny < len(grid[0])
                and visited[nx][ny] is False
                and grid[nx][ny] != "X"
            ):
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
                visited[nx][ny] = True
    
    return -1

def solution(maps):
    grid = [list(m) for m in maps]
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] == "E":
                end = (i, j)
            elif grid[i][j] == "L":
                lever = (i, j)
    
    first = bfs(grid, start, lever)
    second = bfs(grid, lever, end)
    
    if first == -1 or second == -1:
        return -1
        
    return first + second