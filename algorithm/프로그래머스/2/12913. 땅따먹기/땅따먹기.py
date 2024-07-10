def solution(land):
    n = len(land)
    dp = [[0] * 4 for _ in range(n)]
    dp[0] = land[0]
    
    for row in range(1, n):
        for i in range(4):
            for j in range(4):
                if i == j:
                    continue
                
                dp[row][i] = max(dp[row][i], dp[row-1][j] + land[row][i])

    return max(dp[-1])