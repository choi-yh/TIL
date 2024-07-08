from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for d in list(permutations(dungeons)):
        tired = k
        cnt = 0
        for need, use in d:
            if tired >= need:
                tired -= use
                cnt += 1
                
        answer = max(answer, cnt)
    
    return answer