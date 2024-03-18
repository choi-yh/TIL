# https://www.acmicpc.net/problem/10942

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
questions = [list(map(int, input().split())) for _ in range(m)]

dp = [[0] * n for _ in range(n)]
for i in range(n-1, -1, -1):
    for j in range(i, n):
        if i == j:
            dp[i][j] = 1
        elif i+1 == j and numbers[i] == numbers[j]:
            dp[i][j] = 1
        elif j - i > 1 and numbers[i] == numbers[j] and dp[i+1][j-1]:
            dp[i][j] = 1

for s, e in questions:
    print(dp[s-1][e-1])
