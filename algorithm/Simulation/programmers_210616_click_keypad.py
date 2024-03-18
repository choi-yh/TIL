# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    
    # 키패드 리스트로 저장
    keypad = [[i + j*3 for i in range(1, 4)] for j in range(3)]
    keypad.append(['*', 0, '#'])
    
    # 시작 위치
    current_left = [3, 0]
    current_right = [3, 2]
    
    for num in numbers:
        # 눌러야 할 숫자의 좌표
        if num == 0:
            x, y = 3, 1
        else:
            x, y  = (num - 1) // 3, (num - 1) % 3
        
        if y == 0: # 왼손
            answer += 'L'
            current_left = [x, y]
        elif y == 2: # 오른손
            answer += 'R'
            current_right = [x, y]
        else:
            left_dist = abs(current_left[0] - x) + abs(current_left[1] - y)
            right_dist = abs(current_right[0] - x) + abs(current_right[1] - y)
            
            if left_dist < right_dist:
                answer += 'L'
                current_left = [x, y]
            elif left_dist > right_dist:
                answer += 'R'
                current_right = [x, y]
            else:
                if hand == 'left':
                    answer += 'L'
                    current_left = [x, y]
                else:
                    answer += 'R'
                    current_right = [x, y]
            
    return answer