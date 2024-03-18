# https://www.acmicpc.net/problem/9084


def solution(coins, m):
    dp = [0] * (m + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, m + 1):
            dp[i] += dp[i - coin]

    return dp[-1]


t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    print(solution(coins, m))
