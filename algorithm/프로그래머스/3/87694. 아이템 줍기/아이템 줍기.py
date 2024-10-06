"""
1. 이동가능한 동선을 먼저 추출
2. 해당 좌표를 기준으로 목적지까지 이동거리를 계산 (bfs)
"""

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # grid 생성
    grid = [[0] * 102 for _ in range(102)]
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if (x1 < i < x2 and y1 < j < y2):  # 사각형 내부
                    grid[i][j] = -1
                else:
                    if grid[i][j] != -1:
                        grid[i][j] = 1
                        
        
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    start = [2 * characterX, 2 * characterY]
    end = [2 * itemX, 2 * itemY]
    
    visited = [[False] * 102 for _ in range(102)]
    visited[start[0]][start[1]] = True
    
    q = deque([[start, 1]])
    while q:
        [x, y], dist = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < 103
                and 0 <= ny < 103
                and visited[nx][ny] is False
                and grid[nx][ny] == 1
            ):
                if [nx, ny] == end:
                    return dist // 2
                
                visited[nx][ny] = True
                q.append([[nx, ny], dist + 1])
    
    return 0