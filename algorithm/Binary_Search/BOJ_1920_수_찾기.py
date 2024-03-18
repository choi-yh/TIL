# https://www.acmicpc.net/problem/1920


def bst(target, nums):
    start = 0
    end = len(nums) - 1
    if target == nums[start] or target == nums[end]:
        return 1

    while start <= end:
        mid = (start + end) // 2
        if target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            start = mid + 1
        else:
            return 1
    return 0


n = int(input())
nums = sorted(list(map(int, input().split())))
m = int(input())
target_nums = list(map(int, input().split()))

for target_num in target_nums:
    print(bst(target_num, nums))
