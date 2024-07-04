def get_gcd(a, b):
    a, b = min(a, b), max(a, b)
    while True:
        if b % a == 0:
            return a
        
        a, b = b % a, a
        
def get_lcm(a, b):
    gcd = get_gcd(a, b)
    return (a * b) // gcd

def solution(arr):
    lcm = arr[0]
    for i in range(1, len(arr)):
        lcm = get_lcm(lcm, arr[i])
        print(lcm) 
    
    return lcm