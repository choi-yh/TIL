def solution(elements):
    sub_sum_list = elements[:]
    for sub_length in range(2, len(elements)+1):
        summ = sum(elements[:sub_length])
        
        sub_sum_list.append(summ)
        for i in range(len(elements)):
            summ -= elements[i]
            
            sum_idx = i + sub_length
            if sum_idx >= len(elements):
                sum_idx = sum_idx - len(elements)
            
            summ += elements[sum_idx]
            sub_sum_list.append(summ)
        
    return len(set(sub_sum_list))