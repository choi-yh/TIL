def solution(n, s):
    if n > s:
        return [-1]
    
    answer = [0] * n
    for i in range(n):
        answer[i] = s // (n - i)
        s -= answer[i]
    
    return answer