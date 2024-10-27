def solution(n, times):
    left, right = 0, n * max(times)
    while left <= right:
        mid = (left + right) // 2
        total = sum([mid // time for time in times])
        if total < n:
            left = mid + 1
        else:
            right = mid - 1
    
    return right + 1