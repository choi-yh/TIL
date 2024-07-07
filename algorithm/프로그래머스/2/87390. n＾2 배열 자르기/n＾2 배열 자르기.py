"""
n = 3: 
    [
        [1, 2, 3],
        [2, 2, 3],
        [3, 3, 3]
    ]
    -> [1, 2, 3, 2, 2, 3, 3, 3, 3]
    -> [3, 2, 2, 3]
    
n = 4:
    [
        [1, 2, 3, 4],
        [2, 2, 3, 4],
        [3, 3, 3, 4],
        [4, 4, 4, 4]
    ]
    -> [1, 2, 3, 4, 2, 2, 3, 4, 3, 3, 3, 4, 4, 4, 4, 4]
    -> [4, 3, 3, 3, 4, 4, 4, 4]
"""

def solution(n, left, right):
    # n * k + a = left -> k = (left - a) / k
    left_row = left // n
    left_col = left - n * left_row
    
    right_row = right // n
    right_col = right - n * right_row
    
    answer = []
    for row in range(left_row, right_row + 1):
        add_row = [row + 1] * (row + 1) + [i for i in range(row + 2, n + 1)]
        answer += add_row
    
    if right_col - n + 1 == 0:
        return answer[left_col:]
    
    return answer[left_col: right_col - n + 1]