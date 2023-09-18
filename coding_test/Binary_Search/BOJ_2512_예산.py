# https://www.acmicpc.net/problem/2512

n = int(input())
budgets = list(map(int, input().split()))
m = int(input())

def check_budget(budgets, m, mid):
    res = 0
    for budget in budgets:
        if budget >= mid:
            res += mid
        else:
            res += budget
    
    if res > m:
        return False
    return True


start = 0
end = max(budgets)
while start <= end :
    mid = (start + end) // 2
    if check_budget(budgets, m, mid):
        start  = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)