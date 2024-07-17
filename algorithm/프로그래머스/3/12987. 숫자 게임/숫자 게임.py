def solution(A, B):
    answer = 0
    
    a = sorted(A, reverse=True)
    b = sorted(B)
    
    for score in a:
        if score < b[-1]:
            answer += 1
            b.pop()
    
    return answer