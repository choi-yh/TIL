from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dist = [[0] * m for _ in range(n)]
    dist[0][0] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque([[0, 0]])
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < m
                and maps[nx][ny] == 1
                and dist[nx][ny] == 0
            ):
                if (nx, ny) == (n - 1, m - 1):
                    return dist[x][y] + 1
                
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx, ny])
        
    return -1