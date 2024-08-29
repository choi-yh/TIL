import math

def solution(n, k):
    answer = []
    
    arr = list(range(1, n + 1))
    while arr:
        idx = (k - 1) // math.factorial(n - 1)
        answer.append(arr.pop(idx))
        
        k %= math.factorial(n - 1)
        n -= 1
    
    return answer