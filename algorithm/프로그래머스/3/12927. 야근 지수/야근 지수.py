import heapq

def solution(n, works):
    answer = 0
    
    hq = [-1 * work for work in works]
    heapq.heapify(hq)
    
    for _ in range(n):
        work = heapq.heappop(hq)
        if work == 0:
            return 0
        
        work += 1
        heapq.heappush(hq, work)
        
    for remain_work in hq:
        answer += (-1 * remain_work) ** 2
    
    return answer