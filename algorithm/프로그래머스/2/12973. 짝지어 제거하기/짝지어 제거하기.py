def remove_pair(s):
    stack = []
    
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
            continue
            
        if stack[-1] == s[i]:
            stack.pop()
            continue
        
        stack.append(s[i])
        
    return ''.join(stack)

def solution(s):
    while True:
        if len(s) == 0:
            return 1
        
        new_s = remove_pair(s)
        if len(s) == len(new_s):
            return 0
        
        s = new_s