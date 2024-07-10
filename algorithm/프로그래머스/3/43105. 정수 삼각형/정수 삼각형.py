def solution(triangle):
    dp = [[0] * (i + 1) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    
    for depth, values in enumerate(triangle):
        for i, v in enumerate(values):
            if i == 0:
                dp[depth][i] = dp[depth-1][i] + v
            elif i == len(values) - 1:
                dp[depth][i] = dp[depth-1][i-1] + v
            else:
                dp[depth][i] = max(dp[depth-1][i-1], dp[depth-1][i]) + v
    
    return max(dp[-1])