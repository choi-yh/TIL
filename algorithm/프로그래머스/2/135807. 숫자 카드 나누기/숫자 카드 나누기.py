def get_gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b > 0:
        a, b = b, a % b
        
    return a

def get_arr_gcd(arr):
    gcd = arr[0]
    for i in range(1, len(arr)):
        gcd = get_gcd(gcd, arr[i])
        
    return gcd

def solution(arrayA, arrayB):
    answer = 0
    
    if len(set(arrayA).intersection(arrayB)) > 0:
        return 0
    
    a_gcd = get_arr_gcd(arrayA)
    b_gcd = get_arr_gcd(arrayB)
    
    flag = True
    for a in arrayA:
        if a > b_gcd and a % b_gcd == 0:
            flag = False
            break
    
    if flag:
        answer = b_gcd
        
    flag = True
    for b in arrayB:
        if b > a_gcd and b % a_gcd == 0:
            flag = False
            break
            
    if flag:
        answer = max(answer, a_gcd)
    
    return answer