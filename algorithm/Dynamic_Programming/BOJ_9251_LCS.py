# https://www.acmicpc.net/problem/9251


def lcs(x, y):
    x = " " + x
    y = " " + y
    dp = [[0] * len(y) for _ in range(len(x))]
    
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(x)-1][len(y)-1] - 1


x = input()
y = input()

print(lcs(x, y))
