def solution(msg):
    answer = []
    
    dic = {v: i + 1 for i, v in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    next_idx = 27
    
    start = 0
    while start < len(msg):
        for i in range(len(msg), start, -1):
            w = msg[start:i]
            if w in dic.keys():
                answer.append(dic[w])
                
                if i < len(msg):
                    dic[w + msg[i]] = next_idx
                    next_idx += 1
                    
                start = i
                break
    
    return answer