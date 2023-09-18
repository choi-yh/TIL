# https://www.acmicpc.net/problem/2580


def check_row(row, value):
    if value in sudoku[row]:
        return False
    return True


def check_col(col, val):
    for i in range(9):
        if val == sudoku[i][col]:
            return False
    return True


def check_square(row, col, val):
    for i in range(row // 3 * 3, row // 3 * 3 + 3):
        for j in range(col // 3 * 3, col // 3 * 3 + 3):
            if val == sudoku[i][j]:
                return False
    return True


def solve_sudoku(depth):
    global flag

    if depth == len(blanks):  # 빈칸에 있는 값을 모두 채운 경우
        flag = True
        for row in sudoku:
            print(" ".join(map(str, row)))
        return

    if flag:
        return
    else:
        x, y = blanks[depth]  # 현재 채울 위치
        for val in range(1, 10):
            if check_row(x, val) and check_col(y, val) and check_square(x, y, val):
                sudoku[x][y] = val
                solve_sudoku(depth + 1)
                sudoku[x][y] = 0


sudoku = [list(map(int, input().split())) for _ in range(9)]
blanks = [[i, j] for i in range(9) for j in range(9) if sudoku[i][j] == 0]

flag = False # 스도쿠 완성을 확인하기 위함
solve_sudoku(0)
