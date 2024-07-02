def solution(n, computers):
    answer = 0
    
    visited = [False] * (n)
    for i in range(n):
        if visited[i] is False:
            stack = []
            stack.append(i)
            visited[i] = True
            
            while stack:
                cur_computer = stack.pop() # 0
                for connected_computer, status in enumerate(computers[cur_computer]):
                    if visited[connected_computer] is False and status == 1:
                        visited[connected_computer] = True
                        stack.append(connected_computer)
            
            answer += 1
    
    return answer