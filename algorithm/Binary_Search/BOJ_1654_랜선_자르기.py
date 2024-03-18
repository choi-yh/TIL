# https://www.acmicpc.net/problem/1654

k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]

def max_lan(n, lans):
    answer = 0
    
    start = 1
    end = max(lans)
    while start <= end:
        mid = (start + end) // 2
        cut_count = sum([lan // mid for lan in lans])
        
        if cut_count < n:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid    
    return answer

print(max_lan(n, lans))

if __name__ == "__main__":
    k, n = 4, 11
    lans = [802, 743, 457, 539]
    print(max_lan(n, lans))