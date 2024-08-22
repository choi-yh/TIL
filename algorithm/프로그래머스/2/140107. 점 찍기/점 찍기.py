"""
1 <= k <= 1,000,000 이니 O(N^2) 로는 안될 것이다.
원의 방정식: x^2 + y^2 = d^2 1사분면 내부에 있는 점
    (i * k)^2 + (j * k)^2 <= d^2 인 값
    (j*k)^2 <= d**2 - (i * k)^2
    j * k <= math.isqrt(d^2 - (i * k)^2)
    j <= math.isqrt(d^2 - (i * k)^2) / k (0도 포함해야 함)
"""
import math

def solution(k, d):
    answer = 0
    
    for i in range((d // k) + 1):
        answer += math.isqrt(d**2 - (i * k)**2) // k + 1
        
    return answer