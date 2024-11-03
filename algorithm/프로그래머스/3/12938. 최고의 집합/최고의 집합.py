def solution(n, s):
    # n 이 더 큰 경우는 불가능 (1 * n > s)
    if n > s:
        return [-1]
    
    answer = [0] * n
    for i in range(n):
        answer[i] = s // (n - i)  # 남은 갯수로 나누기
        s -= answer[i]
    
    return answer