"""
dfs 로 최소 경로를 탐색. 하지만 코너 수는 더 적어야한다.
이전 두개의 좌표를 가지고 직선인지 코너인지 확인한다. (경로를 담고있는 리스트 필요)

시간 초과... 흠

방향을 가지고 bfs 로 cost 를 갱신해주자. (dp 식으로 계산)
방문하지 않은 경우는 현재 cost 추가,
방문한 경우에는 기존의 cost 와 추가될 cost 를 비교.
"""

import sys
from collections import deque

def bfs(board, start):
    n = len(board)
    
    dp = [[sys.maxsize] * n for _ in range(n)]
    dp[0][0] = 0
    
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    q = deque([start])
    while q:
        x, y, d, cost = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if (
                0 <= nx < n
                and 0 <= ny < n
                and board[nx][ny] == 0
            ):
                next_cost = cost + 100 if d == i else cost + 600
                if dp[nx][ny] > next_cost:
                    dp[nx][ny] = next_cost
                    q.append((nx, ny, i, next_cost))
                    
    return dp[n-1][n-1]

def solution(board):
    return min(bfs(board, (0, 0, 1, 0)), bfs(board, (0, 0, 3, 0)))