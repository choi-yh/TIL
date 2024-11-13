import sys

n, k = map(int, sys.stdin.readline().split(" "))
data = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(n)]
data.sort(key=lambda x: (-x[1], -x[2], -x[3]))

ranking = [0] * (n + 1)
dp = [0] * n
for i in range(n):
    if dp[i] != 0:
        continue

    rank = i + 1
    for j in range(i, n):
        if data[i][1] == data[j][1] and data[i][2] == data[j][2] and data[i][3] == data[j][3]:
            dp[j] = rank
            ranking[data[j][0]] = rank

print(ranking[k])
