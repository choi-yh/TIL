from collections import defaultdict

def solution(gems):
    answer = [1, len(gems)]
    
    kinds = set(gems)
    d = defaultdict(int)
    d[gems[0]] += 1
    
    start, end = 0, 0
    while start <= end:
        if len(d.keys()) == len(kinds):
            if (end - start) < (answer[1] - answer[0]):
                answer = [start + 1, end + 1]
            
            d[gems[start]] -= 1
            if d[gems[start]] == 0:
                del d[gems[start]]
            start += 1
            continue
            
        if end == len(gems) - 1:
            d[gems[start]] -= 1
            if d[gems[start]] == 0:
                del d[gems[start]]
                
            start += 1
            continue
        
        if len(d.keys()) < len(kinds):
            end += 1
            d[gems[end]] += 1
    
    return answer