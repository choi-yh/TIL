# https://www.acmicpc.net/problem/10610

n = str(input())

def thirty(n):
    # 30의 배수인지 체크
    if '0' not in n or sum(list(map(int, n))) % 3 != 0:
        return -1
    else:
        n = sorted(list(n), reverse=True)
        return int(''.join(n))
        
print(thirty(n))
    

if __name__ == "__main__":
    n = str(80875542)
    print(thirty(n))