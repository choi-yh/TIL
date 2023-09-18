# https://www.acmicpc.net/problem/1806

def partial_sum(n, s, seq):
    answer = 100001
    
    start, end, res = 0, 0, 0
    while True:
        if res >= s:
            res -= seq[start]
            start += 1
            answer = min(answer, end - start + 1)
        else:
            if end == n:
                break
            else:
                res += seq[end]
                end += 1

    if answer == 100001:
        return 0
    else:
        return answer

n, s = map(int, input().split())
seq = list(map(int, input().split()))
print(partial_sum(n, s, seq))
