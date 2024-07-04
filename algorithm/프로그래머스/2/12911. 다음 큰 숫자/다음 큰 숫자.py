def solution(n):
    target = str(bin(n)).count("1")
    
    next_num = n + 1
    while True:
        cnt = str(bin(next_num)).count("1")
        if cnt == target:
            return next_num
        
        next_num += 1