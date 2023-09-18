# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    index_list = [i for i in range(len(priorities))]
    answer_list = [i for i in range(len(priorities))]
    
    cnt = 1
    while priorities:
        maxx = max(priorities)
        cur_pri = priorities.pop(0)
        cur_index = index_list.pop(0)
        if cur_pri >= maxx:
            answer_list[cur_index] = cnt
            cnt += 1
        else:
            priorities.append(cur_pri)
            index_list.append(cur_index)
    
    answer = answer_list[location]
    return answer