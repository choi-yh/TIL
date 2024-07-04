def solution(n):
    answer = 0
    
    nums = [i for i in range(1, n+1)]
    
    start, end = 0, 0
    summ = 1
    while start < n:
        if end == n-1:
            if summ == n:
                answer += 1
            
            summ -= nums[start]
            start += 1
            continue
        
        if summ == n:
            answer += 1
            end += 1
            summ += nums[end]
        elif summ < n:
            end += 1
            summ += nums[end]
        else:
            summ -= nums[start]
            start += 1
    
    return answer