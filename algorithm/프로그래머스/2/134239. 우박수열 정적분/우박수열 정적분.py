def cal(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def solution(k, ranges):
    answer = []
    
    # 우박 수열과 각 면적 계산
    areas = [0.0]
    seq = [[0, k]]
    x = 1
    while k > 1:
        k = cal(k)
        seq.append([x, k])
        
        x += 1
        
        area = (k + seq[-2][1]) / 2
        areas.append(area)
    
    # range 별 면적 계산
    for r in ranges:
        x1, x2 = r[0], x + r[1] - 1
        
        if x1 > x2:
            answer.append(-1.0)
        elif x1 == x2:
            answer.append(0.0)
        else:
            answer.append(sum(areas[x1 + 1: x2 + 1]))
        
    return answer