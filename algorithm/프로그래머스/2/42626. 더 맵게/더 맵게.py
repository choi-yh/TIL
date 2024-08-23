import heapq as hq

def solution(scoville, K):
    answer = 0
    
    hq.heapify(scoville)
    
    while True:
        if len(scoville) == 1: # 더 이상 만들 수 없는 경우
            if scoville[0] < K:
                return -1
            else:
                return answer
        
        first = hq.heappop(scoville)
        second = hq.heappop(scoville)
        
        if first >= K:
            return answer
        
        new = first + 2 * second
        hq.heappush(scoville, new)
        
        answer += 1
    
    return -1