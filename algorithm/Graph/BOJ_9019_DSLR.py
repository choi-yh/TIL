# https://www.acmicpc.net/problem/9019

from collections import deque


def cal_d(n):
    return 2 * n % 10000


def cal_s(n):
    n -= 1
    if n == -1:
        n = 9999
    return n


def cal_l(n):
    return n // 1000 + n % 1000 * 10


def cal_r(n):
    return 1000 * (n % 10) + n // 10

# n = 16
# print(cal_d(n))
# print(cal_s(n))
# print(cal_l(n))
# print(cal_r(n))


def main(a, b):
    calc = {
        "D": cal_d,
        "S": cal_s,
        "L": cal_l,
        "R": cal_r
    }

    q = deque()
    answer = ""
    q.append([a, answer])
    visit = [0] * 10001
    visit[a] = 1
    while True:
        num, answer = q.popleft()
        if num == b:
            return answer

        for command, func in calc.items():
            new_num = func(num)
            if not visit[new_num]:
                q.append([new_num, answer + command])
                visit[new_num] = 1


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(main(a, b))
