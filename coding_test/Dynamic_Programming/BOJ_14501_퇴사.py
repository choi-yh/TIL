# https://www.acmicpc.net/problem/14501

def get_max_money(n, schedules):
    dp = [0] * (n+1)
    
    for i in range(n-1, -1, -1):
        if schedules[i][0] + i > n:
            dp[i] = dp[i+1]
        else:
            dp[i] = max(dp[i+1], schedules[i][1] + dp[i + schedules[i][0]])
    
    return dp[0]

n = int(input())
schedules = [list(map(int, input().split())) for _ in range(n)]

print(get_max_money(n, schedules))
