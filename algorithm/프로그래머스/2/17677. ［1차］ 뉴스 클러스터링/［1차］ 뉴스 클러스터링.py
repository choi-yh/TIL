from collections import Counter

def get_multi_set(s):
    ms = []
    
    for i in range(len(s)-1):
        if s[i].isalpha() and s[i+1].isalpha():
            ms.append(s[i:i+2].lower())
    
    return ms

def solution(str1, str2):
    a_ms = get_multi_set(str1)
    b_ms = get_multi_set(str2)
    
    if len(a_ms) == 0 and len(b_ms) == 0:
        return 65536
    
    a_counter = Counter(a_ms)
    b_counter = Counter(b_ms)
    print(a_counter, b_counter)
    
    intersection = set(a_counter.keys()).intersection(set(b_counter.keys()))
    union = set(a_counter.keys()).union(set(b_counter.keys()))
    
    i_cnt = 0
    for i in intersection:
        i_cnt += min(a_counter[i], b_counter[i])
        
    u_cnt = 0
    for u in union:
        if u in a_counter.keys() and u in b_counter.keys():
            u_cnt += max(a_counter[u], b_counter[u])
        elif u in a_counter.keys():
            u_cnt += a_counter[u]
        else:
            u_cnt += b_counter[u]
    
    return int(i_cnt / u_cnt * 65536)