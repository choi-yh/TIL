# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    """
    현재 스테이지의 유저 수 (해당 스테이지를 클리어하지 못한 유저 수)
    해당 스테이지를 클리어한 유저 수 -> 현재 스테이지 이후의 유저 수 합
    """
    answer = []
    num_users = len(stages) # 전체 유저 수

    stage_users = [stages.count(i) for i in range(1, N+2)] # 현재 스테이지의 유저 수
    challenge_users = [sum(stage_users[i:]) for i in range(N+1)] # 해당 스테이지를 도전한 유저 수
    challenge_users.pop() # 최종 스테이지까지 클리어한 유저 수 제거

    fail_ratio = [(i+1, stage_users[i] / challenge_users[i]) if challenge_users[i] != 0 else (i+1, 0) for i in range(N)]
    
    # 실패율 기준으로 정렬
    answer = [i[0] for i in sorted(fail_ratio, key=lambda x: x[1], reverse=True)]
    
    return answer