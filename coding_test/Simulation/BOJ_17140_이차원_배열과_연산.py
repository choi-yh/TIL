# https://www.acmicpc.net/problem/17140

from collections import Counter


def sort_array(array):
    array_cnt = sorted(Counter(array).items(), key=lambda x: (x[1], x[0]))
    new_array = []
    for num, cnt in array_cnt:
        if num:  # 0 제외
            new_array.extend([num, cnt])

    return new_array[:100]


def fill_zero(matrix):
    max_row = 0
    for row in matrix:  # 가장 긴 행 확인
        if len(row) > max_row:
            max_row = len(row)

    # 0 채워넣기
    for row in matrix:
        row.extend([0] * (max_row - len(row)))

    return matrix


def transpose(matrix):
    row, col = len(matrix), len(matrix[0])
    new_matrix = [[0] * row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


def operation(matrix):
    row, col = len(matrix), len(matrix[0])

    new_matrix = []
    if row >= col:
        new_matrix = [sort_array(row) for row in matrix]
        new_matrix = fill_zero(new_matrix)
    else:
        new_matrix = [sort_array(row) for row in transpose(matrix)]
        new_matrix = fill_zero(new_matrix)
        new_matrix = transpose(new_matrix)  # 원래대로 transpose
    return new_matrix


r, c, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(3)]
time = 0
while time <= 100:
    try:
        if a[r - 1][c - 1] == k:
            print(time)
            break
    except:
        pass
    time += 1
    a = operation(a)

if time > 100:
    print(-1)
