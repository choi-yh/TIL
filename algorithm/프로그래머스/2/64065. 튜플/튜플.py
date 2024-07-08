def solution(s):
    # 집합 추출 및 길이 정렬
    stack = []
    sets = []
    for i in range(1, len(s) - 1):
        if s[i] == "}":
            sets.append(list(map(int, ''.join(stack[1:]).split(","))))
            stack = []
        elif len(stack) == 0 and s[i] == ",":
            continue
        else:
            stack.append(s[i])
        
    sorted_sets = sorted(sets, key=lambda x: len(x))
    
    # 결과
    answer = sorted_sets[0]
    for i in range(len(sorted_sets) - 1):
        answer.extend(set(sorted_sets[i+1]) - set(sorted_sets[i]))
    
    return answer