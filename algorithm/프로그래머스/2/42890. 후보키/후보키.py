"""
col 의 길이가 1 ~ 8 이하이므로 1부터 8까지 조합을 구해서 set 에 넣는다.
해당 길이가 row 와 같으면 pk 로 사용 가능
다만, 최소성도 만족해야하므로 해당 조합이 pk 가 되는 경우, 기존 후보키들의 값이 존재하는지 확인한다.
"""

from itertools import combinations

def extract_values(relation, columns):
    return [ tuple(row[col] for col in columns) for row in relation ]

def check_comb(answer, c):
    for ans in answer:
        if set(ans) <= set(c):
            return False
        
    return True

def solution(relation):
    answer = []
    
    row, col = len(relation), len(relation[0])
    for i in range(1, col + 1):
        comb = list(combinations(list(range(col)), i))
        for c in comb:
            if check_comb(answer, c):
                values = extract_values(relation, c)
                if row == len(set(values)):
                    answer.append(c)
    
    return len(answer)