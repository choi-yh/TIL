"""
임의의 포인트 하나를 잡아서 사이클을 만든다.
dfs 문제로 풀면 될듯 함
"""

def solution(cards):
    answer = 0
    
    groups = []
    
    visited = [False] * len(cards)
    for i in range(len(cards)):
        group = []
        
        idx = i
        while visited[idx] is False:
            visited[idx] = True
            
            group.append(idx)
            idx = cards[idx] - 1
            
        if len(group) > 0:
            groups.append(group)
        
    groups.sort(reverse=True, key=lambda x: len(x))
    if len(groups) == 1:
        return 0
    
    return len(groups[0]) * len(groups[1])