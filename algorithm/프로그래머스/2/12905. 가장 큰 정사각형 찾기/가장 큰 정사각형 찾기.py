def solution(board):
    answer = 0

    row = len(board)
    col = len(board[0])
    
    if row == 1 or col == 1:
        return max(board[0])
    
    dp = [[board[i][j] for j in range(col)] for i in range(row)]
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] == 0:
                continue
                
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            
            answer = max(answer, dp[i][j] ** 2)
            
    return answer