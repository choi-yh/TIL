import sys


def solution(n, m, nums):
    answer = 0

    v = nums[0]
    start, end = 0, 0
    while start < n:
        if v == M:
            answer += 1

        if end == n - 1:
            v -= nums[start]
            start += 1
            continue

        if v < m:
            end += 1
            v += nums[end]
        else:
            v -= nums[start]
            start += 1

    return answer


N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

print(solution(N, M, nums))
