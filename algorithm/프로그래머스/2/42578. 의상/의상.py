from collections import defaultdict
from itertools import combinations

def solution(clothes):
    answer = 1
    
    d = defaultdict(list)
    for cloth, kind in clothes:
        d[kind].append(cloth)
    
    for v in d.values():
        answer *= len(v) + 1
    
    return answer - 1