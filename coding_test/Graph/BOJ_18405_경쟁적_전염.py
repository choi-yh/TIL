# https://www.acmicpc.net/problem/18405
"""1초마다 시험관 상태 확인"""

from collections import deque


def spreading(targets):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    next_targets = deque()

    while targets:
        virus, x, y = targets.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and grids[nx][ny] == 0:
                grids[nx][ny] = virus
                next_targets.append([virus, nx, ny])

    return next_targets


n, k = map(int, input().split())
grids = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

targets = deque(
    sorted(
        [[grids[i][j], i, j] for i in range(n) for j in range(n) if grids[i][j]],
        key=lambda x: x[0],
    )
)

for _ in range(s):
    targets = spreading(targets)

print(grids[x - 1][y - 1])
