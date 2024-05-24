func uniquePaths(m int, n int) int {
    dp := make([][]int, m)
    for i := range dp {
        dp[i] = make([]int, n)
    }
    dp[0][0] = 1

    for i := range m {
        for j := range n {
            if i == 0 && j == 0 {
                continue
            } else if i == 0 {
                dp[i][j] = dp[i][j-1]
            } else if j == 0 {
                dp[i][j] = dp[i-1][j]
            } else {
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            }
        }
    }

    return dp[m-1][n-1]
}
