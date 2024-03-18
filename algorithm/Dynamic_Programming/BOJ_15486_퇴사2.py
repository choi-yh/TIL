# https://www.acmicpc.net/problem/15486

def get_money(n, s):
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        t_i, p_i = s[i]

        if t_i + i > n:
            dp[i] = dp[i + 1]
        else:
            dp[i] = max(dp[i + 1], p_i + dp[i + t_i])

    return dp[0]


N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]

print(get_money(N, schedules))
