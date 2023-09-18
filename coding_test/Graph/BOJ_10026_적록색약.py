# https://www.acmicpc.net/problem/10026

from collections import deque


def find_sector(n, drawing):
    sectors = 0
    visit = [[0] * n for _ in range(n)]
    q = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:  # 새로운 구역 발견
                visit[i][j] = 1
                sectors += 1
                color = drawing[i][j]
                q.append([i, j])
                while q:  # BFS 시작
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx >= 0 and nx < n and ny >= 0 and ny < n and drawing[nx][ny] == color and visit[nx][ny] == 0:
                            visit[nx][ny] = 1
                            q.append([nx, ny])
    return sectors


n = int(input())
normal = [list(input()) for _ in range(n)]
color_weak = [["R" if row[i] == "R" or row[i] ==
               "G" else "B" for i in range(n)] for row in normal]

print(find_sector(n, normal), end=' ')
print(find_sector(n, color_weak))