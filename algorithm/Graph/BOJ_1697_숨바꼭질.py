# https://www.acmicpc.net/problem/1697

from collections import deque

n, k = map(int, input().split())
answer = 0
moves = deque([n])
distance = [-1] * 100001
distance[n] = 0

while moves:
    x = moves.popleft()
    left, right, jump = x - 1, x + 1, x * 2
    if k == x:
        print(distance[k])
        break

    for nx in [x - 1, x + 1, x * 2]:
        if nx >= 0 and nx <= 100000 and distance[nx] == -1:
            moves.append(nx)
            distance[nx] = distance[x] + 1
