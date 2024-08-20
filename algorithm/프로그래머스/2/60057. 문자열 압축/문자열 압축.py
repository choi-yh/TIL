def solution(s):
    answer = len(s)
    
    for i in range(1, len(s) // 2 + 1):
        compressed_word = ""
        cur_word = s[:i]
        cnt = 1
        
        for j in range(i, len(s) + i, i):
            next_word = s[j: j + i]
            if next_word == cur_word:
                cnt += 1
            else:
                compressed_word += cur_word if cnt == 1 else str(cnt) + cur_word
                
                cnt = 1
                cur_word = next_word
        
        answer = min(answer, len(compressed_word))
    
    return answer