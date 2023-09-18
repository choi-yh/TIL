# https://programmers.co.kr/learn/courses/30/lessons/43165


def cal_sum(num, res=[0]):
    pos_res = [i + num for i in res]
    neg_res = [i - num for i in res]
    return pos_res + neg_res


def solution(numbers, target):
    res = [0]
    for num in numbers:
        res = cal_sum(num, res)
    answer = res.count(target)
    return answer
