import sys

N = int(sys.stdin.readline())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lines.sort()

dp = [1] * N
for i in range(N):
    for j in range(i):
        if lines[j][1] < lines[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
