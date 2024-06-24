import heapq

def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    
    answer = 0
    pq = []
    for i, e in enumerate(enemy):
        heapq.heappush(pq, -1 * e)
        n -= e
        
        if n < 0:
            if k == 0:
                break
                
            save = -1 * heapq.heappop(pq)
            n += save
            k -= 1
            
        answer += 1
                
    return answer