"""
1. 문자열 두개가 주어졌을 때, 밴을 할 수 있는 아이딘지 판별하는 함수 필요
2. 재귀로 풀어야할 것 같다. 왜냐, ["frodo", "fradi"]가 있고, "fr*d*" 가 밴일 때 두가지 경우에 포함될 수 있기 때문
    banned_id 를 기준으로 user_id 를 순회하면서 후보군을 찾는다. (user_id 배열의 크기가 8 이하라 시간복잡도 고려하지 않아도 괜찮을듯)
    user_check 배열을 만들어서 재귀로 돌린다.
"""

def is_banned(u, b):
    if len(u) != len(b):
        return False
    
    for i in range(len(u)):
        if b[i] == "*":
            continue
            
        if u[i] != b[i]:
            return False

    return True
        

def get_ban(user_id, banned_id, ban_set):
    global result
    
    if len(ban_set) == len(banned_id):
        if sorted(ban_set) not in result:
            result.append(sorted(ban_set))
            
        return
    
    idx = len(ban_set)
    ban = banned_id[idx]
    
    for i, user in enumerate(user_id):
        # 밴된 유저 아이디는 제외
        if user in ban_set:
            continue

        if is_banned(user, ban):
            ban_set.append(user)

            get_ban(user_id, banned_id, ban_set)

            ban_set.pop()

result = []
def solution(user_id, banned_id):
    global result
        
    get_ban(user_id, banned_id, [])
    
    return len(result)