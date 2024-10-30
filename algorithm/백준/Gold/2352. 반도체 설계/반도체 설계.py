import sys


def bst(arr, num):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return left


n = int(sys.stdin.readline())
ports = list(map(int, sys.stdin.readline().split()))

dp = [ports[0]]
for port in ports:
    if dp[-1] < port:
        dp.append(port)
    else:
        mid = bst(dp, port)
        dp[mid] = port

print(len(dp))
