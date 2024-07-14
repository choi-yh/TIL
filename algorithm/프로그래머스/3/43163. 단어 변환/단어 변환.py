from collections import deque

def is_changable(src, dst):
    cnt = 0
    for i in range(len(src)):
        if src[i] != dst[i]:
            cnt += 1
            
    return cnt == 1

def solution(begin, target, words):
    dist = {word: 999 for word in words}
    dist[begin] = 0
    
    q = deque()
    q.append(begin)
    while q:
        w = q.popleft()
        if w == target:
            return dist[w]
        
        for word in words:
            if is_changable(w, word) and dist[word] > dist[w]:
                dist[word] = dist[w] + 1
                q.append(word)
        
    return 0