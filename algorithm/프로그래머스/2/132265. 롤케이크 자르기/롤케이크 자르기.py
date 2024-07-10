from collections import Counter

def solution(topping):
    if len(topping) == 1:
        return 0
    
    answer = 0
    
    a = set()
    a.add(topping[0])
    b = set(topping[1:])
    
    a_counter = dict(Counter(a))
    b_counter = dict(Counter(topping[1:]))
    
    if len(a) == len(b):
        answer += 1
        
    for i in range(1, len(topping)):
        cur_topping = topping[i]
        if cur_topping in a:
            a_counter[cur_topping] += 1
        else:
            a_counter[cur_topping] = 1
            a.add(cur_topping)
            
        if cur_topping in b:
            if b_counter[cur_topping] == 1:
                b.remove(cur_topping)
            elif b_counter[cur_topping] > 1:
                b_counter[cur_topping] -= 1
                
        if len(a) == len(b):
            answer += 1
    
    return answer