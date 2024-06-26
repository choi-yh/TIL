def n_queen(board, row):
    global answer
    
    if row == len(board):
        answer += 1
        return
    
    for col in range(len(board)):
        if promising(board, row, col):
            board[row] = col
            n_queen(board, row + 1)
            
def promising(board, row, col):
    for r in range(row):
        c = board[r]
        if c == col or abs(row - r) == abs(col - c):
            return False
    
    return True

def solution(n):
    global answer
    answer = 0
    
    board = [0] * n
    n_queen(board, 0)
    
    return answer