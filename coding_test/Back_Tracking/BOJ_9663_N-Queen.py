# https://www.acmicpc.net/problem/9663

import sys


def check(row):
    for i in range(row):
        if board[row] == board[i] or (abs(board[row] - board[i]) == abs(row - i)):
            return False
    return True


def queen(row):
    global answer

    if row == n:
        answer += 1
    else:
        for i in range(n):
            board[row] = i
            if check(row):
                queen(row + 1)


n = int(sys.stdin.readline())
answer = 0
board = [0] * n

queen(0)
print(answer)
