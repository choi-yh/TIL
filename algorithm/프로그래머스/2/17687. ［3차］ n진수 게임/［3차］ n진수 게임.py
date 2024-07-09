def convert(n, num):
    over = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    
    if n == 0:
        return str(0)
    
    if num == 10:
        return str(num)
    
    value = ""
    while n > 0:
        remain = n % num
        if remain >= 10 and num > 10:
            value += over[remain]
        else:
            value += str(remain)
            
        n = n // num
        
    return value[::-1]
    

def solution(n, t, m, p):
    answer = ''
    
    arr = []
    cycle = t * m
    for i in range(cycle):
        arr.extend(list(convert(i, n)))
    
    for i in range(t):
        answer += arr[i * m + p - 1]
    
    return answer