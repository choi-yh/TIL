import heapq

def solution(operations):
    answer = []
    
    min_heap = []
    max_heap = []
    for operation in operations:
        oper, num = operation.split(" ")
        
        if oper == "I":
            heapq.heappush(min_heap, int(num))
            heapq.heappush(max_heap, -1 * int(num))
        else:
            if len(min_heap) == 0:
                continue
            elif num == "1":
                target = heapq.heappop(max_heap)
                min_heap.remove(-1 * target)
            elif num == "-1":
                target = heapq.heappop(min_heap)
                max_heap.remove(-1 * target)

        
    if len(min_heap) == 0:
        return [0, 0]
        
    return [-1 * heapq.heappop(max_heap), heapq.heappop(min_heap)]