def solution(data, col, row_begin, row_end):
    answer = 0

    # 2. 정렬
    sorted_data = sorted(data, key=lambda x: (x[col-1], -1 * x[0]))
    
    # 4. 연산
    for i in range(row_begin, row_end + 1):
        s_i = sum([v % (i) for v in sorted_data[i - 1]])
        answer = answer ^ s_i
    
    return answer