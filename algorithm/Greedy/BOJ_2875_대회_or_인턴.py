# https://www.acmicpc.net/problem/2875

n, m, k = map(int, input().split())

def make_team(n, m, k):
    while k > 0:
        if n // 2 >= m:
            n -= 1
            k -= 1
        else:
            m -= 1
            k -= 1
    
    return min(n // 2, m)

print(make_team(n, m, k))
    
if __name__ == "__main__":
    n, m, k = 6, 10, 3
    print(make_team(n, m, k))