def solution(book_time):
    answer = 0
    
    for i in range(len(book_time)):
        start, end = book_time[i]
        s_h, s_m = map(int, start.split(":"))
        s = 60 * s_h + s_m
        
        e_h, e_m = map(int, end.split(":"))
        e = 60 * e_h + e_m + 10
        
        book_time[i] = [s, e]
    
    sorted_book_time = sorted(book_time, key=lambda x: (x[0], x[1]))
    
    q = []
    for time in sorted_book_time:
        booked = False
        for i, room in enumerate(q):
            if room[1] <= time[0]:
                q[i] = time
                booked = True
                break
                
        if booked is False:
            q.append(time)
        
        answer = max(answer, len(q))
    
    return answer