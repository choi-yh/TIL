def solution(order):
    answer = 0
    
    rail = [i for i in range(len(order) + 1)]
    sub = []
    
    idx = 0
    for box in order:
        if len(rail) == 0 or idx > box:
            if sub[-1] == box:
                answer += 1
                sub.pop()
                continue
            else:
                return answer
        
        sub.extend(rail[idx:box])
        idx = box + 1
        
        answer += 1
    
    return answer