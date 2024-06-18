def solution(x, y, n):
    maxInt = 1000001
    dp = [maxInt] * (y + 1)
    dp[x] = 0
    
    for i in range(x, y + 1):
        plus = i + n
        double = i * 2
        triple = i * 3
        
        if plus < y + 1:
                dp[plus] = min(dp[plus], dp[i] + 1)
        
        if double < y + 1:
                dp[double] = min(dp[double], dp[i] + 1)
                
        if triple < y + 1:
                dp[triple] = min(dp[triple], dp[i] + 1)
        
    if dp[y] == maxInt:
        return -1
    
    return dp[y]