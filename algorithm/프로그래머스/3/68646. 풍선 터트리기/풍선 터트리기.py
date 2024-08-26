"""
무조건 제거 되는 상황 == 해당 원소를 기준으로 왼쪽의 최솟값과 오른쪽의 최솟값이 모두 해당 원소보다 작다.
(작은 원소를 제거하는 상황은 무조건 한번임)
"""

def solution(a):
    answer = len(a)
    
    leftMin = [1e9] * len(a)
    rightMin = [1e9] * len(a)
    
    lm = a[0]
    leftMin[0] = lm
    for i in range(1, len(a) - 1):
        if a[i] < lm:
            lm = a[i]
            
        leftMin[i] = lm
        
    rm = a[-1]
    rightMin[-1] = rm
    for i in range(len(a) - 1, 0, -1):
        if a[i] < rm:
            rm = a[i]
            
        rightMin[i] = rm
        
    for i in range(len(a)):
        if a[i] > leftMin[i] and a[i] > rightMin[i]:
            answer -= 1
    
    return answer