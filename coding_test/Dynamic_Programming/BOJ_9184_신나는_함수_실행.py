# https://www.acmicpc.net/problem/9184

def get_dp():
    dp = [[[1] * 21 for _ in range(21)] for _ in range(21)]
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):
                if i < j < k:
                    dp[i][j][k] = dp[i][j][k - 1] + dp[i][j - 1][k - 1] - dp[i][j - 1][k]
                else:
                    dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] - dp[i - 1][j - 1][k - 1]

    return dp


def w(a, b, c, dp):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return dp[20][20][20]

    return dp[a][b][c]


DP = get_dp()

while True:
    A, B, C = map(int, input().split())
    if A == -1 and B == -1 and C == -1:
        break

    print(f"w({A}, {B}, {C}) = {w(A, B, C, DP)}")
