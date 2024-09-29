def solution(data):
    answer = 0

    data.sort()

    for i in range(len(data)):
        start, end = 0, len(data) - 1
        while start < end:
            summ = data[start] + data[end]
            if summ == data[i]:
                if i == start:
                    start += 1
                elif i == end:
                    end -= 1
                else:
                    answer += 1
                    break
            elif summ > data[i]:
                end -= 1
            else:
                start += 1

    return answer


T = int(input())
DATA = list(map(int, input().split()))
print(solution(DATA))
