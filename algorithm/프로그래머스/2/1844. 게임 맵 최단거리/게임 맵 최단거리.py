from collections import deque

def solution(maps):
    dist = [[1] * len(maps[0]) for _ in range(len(maps))]
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    visited[0][0] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < len(maps)
                and 0 <= ny < len(maps[0])
                and maps[nx][ny] == 1
                and visited[nx][ny] is False
            ):
                if (nx, ny) == (len(maps) - 1, len(maps[0]) - 1):
                    return dist[x][y] + 1
                
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    
    return -1