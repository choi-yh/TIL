def time_to_min(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def min_to_time(t):
    return "{:02d}:{:02d}".format(t // 60, t % 60)

def solution(n, t, m, timetable):
    tt = [0] * len(timetable)
    for i, time in enumerate(timetable):
        tt[i] = time_to_min(time)
        
    tt = sorted(tt)
            
    shuttles = [9 * 60 + t * i for i in range(n)]
    idx = 0
    for shuttle in shuttles:
        cnt = 0 # 해당 버스에 타는 인원 수
        
        while cnt < m and idx < len(tt) and tt[idx] <= shuttle:
            cnt += 1
            idx += 1
            
        if cnt == m:
            answer = min_to_time(tt[idx-1] - 1)
        else:
            answer = min_to_time(shuttle)
                
    return answer