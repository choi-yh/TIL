# https://www.acmicpc.net/problem/1789

s = int(input())
n = 1
while s >= n:
    s -= n
    n += 1

print(n-1)