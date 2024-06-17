def solution(friends, gifts):
    answer = 0
    
    idx = {friends[i]:i for i in range(len(friends))}
    
    table = [[0] * len(friends) for _ in range(len(friends))]
    for gift in gifts:
        giver, taker = gift.split(" ")
        table[idx[giver]][idx[taker]] += 1
        
    for a in friends: # 받을 사람
        expect = 0 # 받을 선물
        for b in friends:
            if table[idx[a]][idx[b]] > table[idx[b]][idx[a]]:
                expect += 1
            elif table[idx[a]][idx[b]] == table[idx[b]][idx[a]] and get_gift_idx(table, idx[a]) > get_gift_idx(table, idx[b]):
                expect += 1
                
        answer = max(answer, expect)
    
    return answer

def get_gift_idx(table, friend):
    give_count = 0
    take_count = 0
    for i in range(len(table)):
        give_count += table[friend][i]
        take_count += table[i][friend]
        
    return give_count - take_count