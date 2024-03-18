# https://www.acmicpc.net/problem/1018

def get_coloring_board_count(chess_boad):
    b_cnt, w_cnt = 0, 0
    for i in range(8):
        for j in range(8):
            if chess_board[i][j] != b_board[i][j]:
                b_cnt += 1
            if chess_board[i][j] != w_board[i][j]:
                w_cnt += 1

    return min(b_cnt, w_cnt)

n, m = map(int, input().split())
boards = [ list(input()) for _ in range(n) ]

b_board = [ [ "B" if (i + j) % 2 == 0 else "W" for j in range(8) ] for i in range(8) ]
w_board = [ [ "W" if (i + j) % 2 == 0 else "B" for j in range(8) ] for i in range(8) ]

answer = 32
for i in range(m-7):
    for j in range(n-7):
        chess_board = [ row[i:i+8] for row in boards[j:j+8] ]
        answer = min(answer, get_coloring_board_count(chess_board))

print(answer)
