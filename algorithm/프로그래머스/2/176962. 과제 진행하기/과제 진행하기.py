def solution(plans):
    answer = []
    
    sorted_plans = sorted(plans, key=lambda x: x[1])
    for i, plan in enumerate(sorted_plans):
        h, m = plan[1].split(":")
        sorted_plans[i][1] = 60 * int(h) + int(m)
        sorted_plans[i][2] = int(plan[2])
        
    holdings = []
    for i, plan in enumerate(sorted_plans):
        if i == len(sorted_plans) - 1:
            answer.append(plan[0])
            break
            
        next_plan = sorted_plans[i+1]
        if plan[1] + plan[2] <= next_plan[1]:
            answer.append(plan[0])
            remain_time = next_plan[1] - (plan[1] + plan[2])
            while holdings and remain_time > 0:
                hold_plan = holdings.pop()
                if hold_plan[2] <= remain_time:
                    answer.append(hold_plan[0])
                    remain_time -= hold_plan[2]
                else:
                    hold_plan = [hold_plan[0], hold_plan[1], hold_plan[2] - remain_time]
                    remain_time = 0
                    holdings.append(hold_plan)
        else:
            holdings.append([plan[0], plan[1], plan[1] + plan[2] - next_plan[1]])        
                
    while holdings:
        answer.append(holdings.pop()[0])
    
    return answer