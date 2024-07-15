import math

def solution(fees, records):
    answer = []
    
    last_time = 23 * 60 + 59
    
    parking_log = dict()
    for record in records:
        time, car, action = record.split(" ")
        h, m = map(int, time.split(":"))
        t = h * 60 + m
        
        if car in parking_log:
            if action == "IN":
                parking_log[car].append([t, last_time])
            else:
                parking_log[car][-1][1] = t
        else:
            parking_log[car] = [[t, last_time]]
    
    for car in sorted(list(parking_log.keys())):
        total_time = 0
        for log in parking_log[car]:
            total_time += log[1] - log[0]
            
        if total_time < fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((total_time - fees[0]) / fees[2]) * fees[3])
    
    return answer