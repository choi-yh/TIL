import sys

p = int(sys.stdin.readline().rstrip())
for _ in range(p):
    inputs = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    t, nums = inputs[0], inputs[1:]
    count = 0

    sorted_nums = []
    for n in nums:
        sorted_nums.append(n)

        # 정렬
        for i in range(len(sorted_nums) - 1, 0, -1):
            if sorted_nums[i] < sorted_nums[i - 1]:
                sorted_nums[i], sorted_nums[i - 1] = sorted_nums[i - 1], sorted_nums[i]
                count += 1

    print(f"{t} {count}")
