import heapq

"""
1. 현재 시각을 기준으로 했을 때, 가능한 작업을 꺼내고, 그 중에서 소요시간이 적은 작업을 우선적으로 진행한다.

2. 현재 시각보다 작거나 같은 시작 시간이 가능한 작업. -> 이걸 꺼내서 힙에 넣고, 힙이 빌때까지 작업을 돌린다?
"""
def solution(jobs):
    answer = 0
    n = len(jobs)
    
    job_cnt = 0 # 수행한 작업 카운트 (반복문을 진행시키기 위함))
    cur_time = 0 # 현재 시각
    last_work_time = -1 # 작업 대상을 추출하기 위한 마지막 작업 시간
    heapq.heapify(jobs) # 요청 시점을 기준으로 작업 정렬
    
    waiting_jobs = [] # 작업 대상 후보군
    while job_cnt < n:
        for job in jobs:
            if last_work_time < job[0] <= cur_time:
                heapq.heappush(waiting_jobs, [job[1], job[0]])
                
        if len(waiting_jobs) == 0:
            cur_time += 1
            continue
        
        job = heapq.heappop(waiting_jobs)
        
        answer += (cur_time - job[1]) + job[0]
        
        job_cnt += 1
        last_work_time = cur_time
        cur_time += job[0]
    
    return answer // n