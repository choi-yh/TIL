from collections import Counter

def solution(weights):
    answer = 0
    
    keys = set(weights)
    counter = Counter(weights)
    
    for k, v in counter.items():
        if v > 1:
            answer += v * (v - 1) // 2
    
    for i, key in enumerate(keys):
        if key * 2 in keys:
            answer += counter[key] * counter[key * 2]
            
        if key * 3/2 in keys:
            answer += counter[key] * counter[key * 3/2]
            
        if key * 4/3 in keys:
            answer += counter[key] * counter[key * 4/3]
    
    return answer