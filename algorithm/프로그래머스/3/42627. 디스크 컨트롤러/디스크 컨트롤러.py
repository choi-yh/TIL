import heapq as hq

def solution(jobs):
    answer = 0
    
    completed_job_cnt = 0
    job_start_time = 0
    worked_time = -1
    waitings = []
    
    while completed_job_cnt < len(jobs):
        # 작업할 수 있는 대상을 힙에 넣기
        for job in jobs:
            if worked_time < job[0] <= job_start_time:
                hq.heappush(waitings, [job[1], job[0]])
        
        # 작업 대상이 없다면 현재 시간 증가
        if len(waitings) == 0:
            job_start_time += 1
            continue
            
        # 총 소요시간이 적게 걸리는 작업
        j = hq.heappop(waitings)
        
        answer += j[0] + job_start_time - j[1]
        worked_time = job_start_time
        job_start_time += j[0]
        
        completed_job_cnt += 1
    
    return answer // len(jobs)