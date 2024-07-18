def get_bin(num):
    return list(str(bin(num)))[2:]

def solution(numbers):
    answer = []
    
    for number in numbers:        
        if number % 2 == 0:
            answer.append(number + 1)
            continue
        
        bit = ["0"] + get_bin(number)
        for i in range(len(bit) - 1, -1, -1):
            if bit[i] == "0":
                bit[i] = "1"
                bit[i + 1] = "0"
                break
        
        answer.append(int(''.join(bit), 2))
    
    return answer