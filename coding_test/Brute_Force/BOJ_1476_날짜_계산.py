# https://www.acmicpc.net/problem/1476

e, s, m = map(int, input().split())

x, y, z = 1, 1, 1
year = 1
while x != e or y != s or z != m:
    year += 1
    x += 1
    y += 1
    z += 1
    
    if x > 15:
        x = 1
    if y > 28:
        y = 1
    if z > 19:
        z = 1
    
print(year)