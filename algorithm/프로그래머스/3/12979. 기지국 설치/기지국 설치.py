import math

def solution(n, stations, w):
    answer = 0
    
    needed = [[1, n]]
    for s in stations:
        left = max(0, s - w)
        right = min(n, s + w)
        
        if left < needed[-1][1]:
            needed[-1][1] = left - 1
            
        if right < n:
            needed.append([right + 1, n])
        
    for left, right in needed:
        answer += math.ceil((right - left + 1) / (2 * w + 1))
    
    return answer