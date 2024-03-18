# https://www.acmicpc.net/problem/2470

import sys
from collections import deque


def make_zero(n, liquids):
    value = sys.maxsize
    target = deque([liquids[0], liquids[-1]])

    start = 0
    end = n - 1

    while start < end:
        start_value, end_value = liquids[start], liquids[end]
        cur_value = abs(start_value + end_value)

        if cur_value < value:
            value = cur_value
            target = deque([start_value, end_value])

        if start_value + end_value > 0:
            end -= 1
        else:
            start += 1

    return str(target[0]) + ' ' + str(target[1])


N = int(input())
L = sorted(list(map(int, input().split())))

print(make_zero(N, L))

if __name__ == "__main__":
    N = 5
    L = sorted([-2, 4, -99, -1, 98])

    answer = "-99 98"
    print(make_zero(N, L) == answer)
