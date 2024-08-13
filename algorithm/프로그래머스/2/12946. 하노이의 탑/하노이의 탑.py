"""
n-1 개의 원판을 1 -> 2로 이동
1개의 원판을 1 -> 3으로 이동
n-1 개의 원판을 2 -> 3으로 이동
"""
def hanoi(start, end, remain, cnt, answer):
    if cnt == 1:
        answer.append([start, end])
    else:
        hanoi(start, remain, end, cnt - 1, answer)
        hanoi(start, end, remain, 1, answer)
        hanoi(remain, end, start, cnt - 1, answer)
        
    return answer

def solution(n):
    return hanoi(1, 3, 2, n, [])