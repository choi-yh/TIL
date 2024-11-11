import sys

n = int(sys.stdin.readline())
points = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(n)]
points.sort()

lines = 0
start, end = points[0][0], points[0][1]
for x, y in points:
    if x > end:
        lines += end - start
        start = x
        end = y
    elif y > end:
        end = y

print(lines + end - start)
