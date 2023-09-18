# https://www.acmicpc.net/problem/3273

def solution():
    answer = 0

    sorted_nums = sorted(nums)
    left, right = 0, n - 1
    while left < right:
        check = sorted_nums[left] + sorted_nums[right]
        if check == x:
            answer += 1
            left += 1
        elif check > x:
            right -= 1
        elif check < x:
            left += 1

    return answer


n = int(input())
nums = list(map(int, input().split()))
x = int(input())

print(solution())
