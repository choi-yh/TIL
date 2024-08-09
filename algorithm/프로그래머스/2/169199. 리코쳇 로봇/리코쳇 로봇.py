from collections import deque

def solution(board):
    grid = [list(b) for b in board]
    r, c = len(grid), len(grid[0])
    for i in range(r):
        for j in range(c):
            if grid[i][j] == "R":
                start = (i, j, 0)
            
            if grid[i][j] == "G":
                end = (i, j)
                
    visited = [[False] * c for _ in range(r)]
    visited[start[0]][start[1]] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque([start])
    while q:
        x, y, cnt = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 장애물이나 맨 끝은 제외
            if (
                (0 > nx or nx >= r)
                or (0 > ny or ny >= c)
                or grid[nx][ny] == "D"
            ):
                continue
                
            # 끝까지 이동
            while (
                0 <= nx < r
                and 0 <= ny < c
                and grid[nx][ny] != "D"
            ):
                nx, ny = nx + dx[i], ny + dy[i]
                
            # 현재 좌표는 이동할 수 없는 좌표이므로 이전 위치로 이동
            nx, ny = nx - dx[i], ny - dy[i]
            
            # 종점이면 리턴
            if grid[nx][ny] == "G":
                return cnt + 1
            
            # 도달한 적 있는 위치인지 확인
            if visited[nx][ny] is False:
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = True
        
    return -1