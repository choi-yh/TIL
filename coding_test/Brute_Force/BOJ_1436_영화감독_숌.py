# https://www.acmicpc.net/problem/1436

def get_end_number(n):
    num, cnt = 0, 0
    while True:
        num += 1
        if "666" in str(num):
            cnt += 1
        
        if cnt == n:
            return num

n = int(input())
print(get_end_number(n))