"""
1. enroll 과 referral 로 트리 구조를 만들어야할듯함
2. seller 돌면서 그냥 계산 해도 괜찮나? -> 일단 구현 ㄱㄱ
"""
from collections import defaultdict

def cal_amount(am, pm, seller, amount):
    remains = amount // 10
    if remains == 0:
        am[seller] += amount
        return am
        
    amount -= remains
    am[seller] += amount
    p = pm[seller]
    
    while p != "center":
        amount = remains
        remains //= 10
        if remains == 0:
            am[p] += amount
            return am
        
        am[p] += amount - remains
        p = pm[p]
    
    return am

def solution(enroll, referral, seller, amount):
    answer = []
    
    amount_map = defaultdict(int)
    parent_map = defaultdict(str)
    for e, r in zip(enroll, referral):
        if r == "-":
            parent_map[e] = "center"
        else:
            parent_map[e] = r
            
        amount_map[e] = 0
        
    for s, a in zip(seller, amount):
        amount_map = cal_amount(amount_map, parent_map, s, a * 100)
        
    for e in enroll:
        answer.append(amount_map[e])
    
    return answer