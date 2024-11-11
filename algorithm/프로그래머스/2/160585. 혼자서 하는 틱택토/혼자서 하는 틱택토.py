def solution(board):
    o_count, x_count = 0, 0
    for row in board:
        o_count += row.count("O")
        x_count += row.count("X")
        
    if not (o_count == x_count or o_count - x_count == 1):
        return 0
    
    if check_win(board, "O") and check_win(board, "X"):
        return 0
    
    if check_win(board, "O") and o_count == x_count:
        return 0
    
    if check_win(board, "X") and o_count != x_count:
        return 0
    
    return 1

def check_win(board, t):
    for i, row in enumerate(board):
        if row == t * 3:
            return True
        
        col = board[0][i] + board[1][i] + board[2][i]
        if col == t * 3:
            return True
        
    if (
      board[0][0] + board[1][1] + board[2][2] == t * 3
        or board[2][0] + board[1][1] + board[0][2] == t * 3
    ):
        return True
    
    return False