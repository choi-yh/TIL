def solution(gems):
    answer = [1, len(gems)]
    
    gems_set = set(gems)
    
    check_set = set()
    check_set.add(gems[0])
    check_dict = {gem: 0 for gem in gems}
    check_dict[gems[0]] += 1
    
    start = 0
    end = 0
    while start <= end:
        if len(check_set) == len(gems_set) and (end - start) < (answer[1] - answer[0]):
            answer = [start + 1, end + 1]
            
        if end == len(gems) - 1:
            check_dict[gems[start]] -= 1
            if check_dict[gems[start]] == 0 and gems[start] in check_set:
                check_set.remove(gems[start])
                
            start += 1
            continue
            
        if len(check_set) < len(gems_set):
            end += 1
            
            check_dict[gems[end]] += 1
            check_set.add(gems[end])
        else:
            check_dict[gems[start]] -= 1
            if check_dict[gems[start]] == 0 and gems[start] in check_set:
                check_set.remove(gems[start])
                
            start += 1
    
    return answer