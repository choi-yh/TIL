def solution(x, y, n):
    dp = [0] * (y + 1)
    
    for i in range(x, y + 1):
        if i != x and dp[i] == 0:
            dp[i] = -1
            continue
        
        plus = i + n
        double = i * 2
        triple = i * 3
        
        if plus < y + 1:
            if dp[plus] == 0:
                dp[plus] = dp[i] + 1
            else:
                dp[plus] = min(dp[plus], dp[i] + 1)
        
        if double < y + 1:
            if dp[double] == 0:
                dp[double] = dp[i] + 1
            else:
                dp[double] = min(dp[double], dp[i] + 1)
                
        if triple < y + 1:
            if dp[triple] == 0:
                dp[triple] = dp[i] + 1
            else:
                dp[triple] = min(dp[triple], dp[i] + 1)
        
    return dp[y]