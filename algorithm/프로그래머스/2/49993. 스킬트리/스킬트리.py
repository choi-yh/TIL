from collections import deque

def solution(skill, skill_trees):
    answer = 0
    skill_seq = list(skill)
    
    for skill_tree in skill_trees:
        flag = True
        q = deque(skill_seq[:])
        
        for i in range(len(skill_tree)):
            target_skill = skill_tree[i]
            if target_skill in q:
                if target_skill == q[0]:
                    q.popleft()
                else:
                    flag = False
                    break
            
        if flag:
            answer += 1
    
    return answer