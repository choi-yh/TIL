def solution(diffs, times, limit):
    answer = max(diffs)
    
    start, end = 1, max(diffs)
    while start < end:
        level = (start + end) // 2
        if check(level, diffs, times, limit):
            answer = min(level, answer)
            end = level
        else:
            start = level + 1
            
    return answer

# 현재 레벨에서 퍼즐을 풀 수 있는지 계산
def check(level, diffs, times, limit):
    total = 0
    time_prev = 0
    for i, (diff, time) in enumerate(zip(diffs, times)):
        total += get_time(level, diff, time, time_prev)
        if total > limit:
            return False
        
        time_prev = time
    
    return True

# 현재 퍼즐을 푸는데 걸리는 시간 계산
def get_time(level, diff, time_cur, time_prev):
    if diff <= level:
        return time_cur
    else:
        return (diff - level) * (time_cur + time_prev) + time_cur