# https://www.acmicpc.net/problem/2133

def fill_tiles():
    dp = [0] * 31
    dp[0] = 1
    dp[2] = 3

    for i in range(4, 31):
        dp[i] = 3 * dp[i - 2]
        for j in range(4, i + 1, 2):
            dp[i] += 2 * dp[i - j]

    return dp[N]


N = int(input())
print(fill_tiles())
