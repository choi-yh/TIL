# https://www.acmicpc.net/problem/1074

def explore_z(n_square, n, r, c, target):
    while n > 1:
        n_square //= 2
        n -= 1
        if r < n_square and c < n_square:
            pass
        elif r < n_square <= c:
            target += n_square ** 2
            c -= n_square
        elif r >= n_square > c:
            target += n_square ** 2 * 2
            r -= n_square
        elif r >= n_square and c >= n_square:
            target += n_square ** 2 * 3
            r -= n_square
            c -= n_square

    if r == 0 and c == 0:
        print(target)
    elif r == 0 and c == 1:
        print(target + 1)
    elif r == 1 and c == 0:
        print(target + 2)
    elif r == 1 and c == 1:
        print(target + 3)


N, R, C = map(int, input().split())

explore_z(2 ** N, N, R, C, 0)
