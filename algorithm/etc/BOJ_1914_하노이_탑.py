# https://www.acmicpc.net/problem/1914

def hanoi(n):
    if n == 1:
        return 1
    return 2 * hanoi(n-1) + 1

def hanoi_check(n, a, b, c):
    if n == 1:
        print(f"{a} {c}")
    else:
        hanoi_check(n-1, a, c, b)
        hanoi_check(1, a, b, c)
        hanoi_check(n-1, b, a, c)

n = int(input())
if n > 20:
    print(hanoi(n))
else:
    print(hanoi(n))
    hanoi_check(n, 1, 2, 3)