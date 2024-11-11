import sys
import heapq

n, m = map(int, sys.stdin.readline().split(" "))
nums = list(map(int, sys.stdin.readline().split(" ")))

# 가장 작은 수 두개를 사용 -> min heap
heapq.heapify(nums)

for _ in range(m):
    x = heapq.heappop(nums)
    y = heapq.heappop(nums)

    heapq.heappush(nums, x + y)
    heapq.heappush(nums, x + y)

print(sum(nums))
