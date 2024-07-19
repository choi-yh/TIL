def solution(n):
    answer = ''
    
    rules = [1, 2, 4]
    while n > 0:
        q, r = (n - 1) // 3, (n - 1) % 3
        
        answer = str(rules[r]) + answer
        n = q
    
    return answer