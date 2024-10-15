from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    
    sale_rates = [10, 20, 30, 40]
    perms = list(product(sale_rates, repeat=len(emoticons)))
    for perm in perms:
        plus_register_count, amount = 0, 0
        
        for user in users:
            user_amount = 0
            for emoticon, rate in zip(emoticons, perm):
                if rate >= user[0]:
                    user_amount += emoticon * (1 - rate / 100)
                    
            if user_amount >= user[1]:
                plus_register_count += 1
            else:
                amount += user_amount
                
        if plus_register_count > answer[0]:
            answer = [plus_register_count, amount]
        elif plus_register_count == answer[0] and amount > answer[1]:
            answer = [plus_register_count, amount]
    
    return answer