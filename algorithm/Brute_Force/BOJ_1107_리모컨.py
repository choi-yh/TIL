# https://www.acmicpc.net/problem/1107


def check(num):
    for i in str(num):
        if int(i) in broken:
            return False
    return True


n = int(input())
m = int(input())
if m:
    broken = list(map(int, input().split()))
else:
    broken = []

start = 100
answer = abs(n - 100)

for num in range(1000001):
    if check(num):
        answer = min(answer, len(str(num)) + abs(num - n))

print(answer)
