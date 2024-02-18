import sys
sys.setrecursionlimit(10000)

def solution(s):
    answer = 0
    substrings = check_str(s, [])
    
    return len(substrings)

def check_str(s, substrings):
    x = s[0]
    same_count, diff_count = 0, 0
    
    for i in range(len(s)):
        if s[i] == x:
            same_count += 1
        else:
            diff_count += 1
            
        if same_count == diff_count:
            substrings.append(s[:i+1])
            if i == len(s) - 1:
                return substrings
            
            return check_str(s[i+1:], substrings)
    
    substrings.append(s)
    return substrings