import heapq as hq

def solution(operations):
    answer = []
    
    min_q = []
    max_q = []
    
    for oper in operations:
        command, num = oper.split(" ")
        num = int(num)
        
        if command == "I":
            hq.heappush(min_q, num)
            hq.heappush(max_q, -1 * num)
            continue
        
        if len(max_q) == 0:
            continue
            
        if num == 1:
            m = hq.heappop(max_q)
            min_q.remove(-1 * m)
        elif num == -1:
            m = hq.heappop(min_q)
            max_q.remove(-1 * m)
            
    if len(max_q) == 0:
        return [0, 0]
    
    return [-1 * hq.heappop(max_q), hq.heappop(min_q)]