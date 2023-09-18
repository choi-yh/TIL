# https://www.acmicpc.net/problem/10819

from itertools import permutations


def calc(nums):
    result = 0

    for i in range(len(nums) - 1):
        result += abs(nums[i] - nums[i + 1])

    return result


n = int(input())
a = list(map(int, input().split()))
answer = 0

perm = list(permutations(a, n))

for nums in perm:
    res = calc(nums)
    if res > answer:
        answer = res

print(answer)
