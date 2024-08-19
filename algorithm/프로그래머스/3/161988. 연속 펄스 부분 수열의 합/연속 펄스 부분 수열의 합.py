def solution(sequence):
    answer = max(sequence[0], -1 * sequence[0])
    
    dp1 = [0] * len(sequence) # 1 부터 시작
    dp2 = [0] * len(sequence) # -1 부터 시작
    
    dp1[0] = sequence[0]
    dp2[0] = -1 * sequence[0]
    
    purse = -1
    for i in range(1, len(sequence)):
        v = sequence[i]
        
        dp1[i] = max(dp1[i-1] + purse * v, purse * v)
        dp2[i] = max(dp2[i-1] + -1 * purse * v, -1 * purse * v)
        
        answer = max(answer, dp1[i], dp2[i])
        
        purse *= -1
    
    return answer