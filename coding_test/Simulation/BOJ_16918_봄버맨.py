# https://www.acmicpc.net/problem/16918

"""
n이 짝수인 경우, 무조건 모든 격자엔 폭탄이 들어있게 되고,
홀수일 경우 이전 격자 상태에서 상하좌우 폭탄을 제거한 상태가 되므로 연산을 반복
"""
from copy import deepcopy

r, c, n = map(int, input().split())

all = [['O'] * c for _ in range(r)]
start = [list(input()) for _ in range(r)]

def bomb(board):
    "3초 뒤 상황의 격자"
    next = deepcopy(all)
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                next[i][j] = '.'
                if i - 1 >= 0:
                    next[i-1][j] = '.'
                if i + 1 < r:
                    next[i+1][j] = '.'
                if j - 1 >= 0:
                    next[i][j-1] = '.'
                if j + 1 < c:
                    next[i][j+1] = '.'
    return next

time = 1
cur = start
while time < n:
    time += 1
    if time % 2 == 0:
        cur = all
    else:
        cur = bomb(start)
        start = cur

for row in cur:
    print(''.join(row))