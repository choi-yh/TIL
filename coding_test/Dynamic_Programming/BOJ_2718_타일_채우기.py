# https://www.acmicpc.net/problem/2718

def get_dp():
    dp = [0, 1, 5, 11, 36]

    i = 5
    while dp[-1] <= 2 ** 31 - 1:
        cur_value = dp[i - 1] + 5 * dp[i - 2] + dp[i - 3] - dp[i - 4]
        dp.append(cur_value)
        i += 1

    return dp


T = int(input())
DP = get_dp()

for _ in range(T):
    N = int(input())
    print(DP[N])
