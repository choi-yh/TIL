# https://www.acmicpc.net/problem/2110

n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]

def install_router(c, houses):
    answer = 0

    houses = sorted(houses)
    start = 1
    end = houses[-1] - houses[0]

    while start <= end:
        mid = (start + end) // 2
        
        installed_house = houses[0]
        cnt = 1
        for i in range(1, len(houses)):
            if houses[i] >= installed_house + mid:
                installed_house = houses[i]
                cnt += 1
        if cnt >= c:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
        
    return answer

print(install_router(c, houses))


if __name__ == "__main__":
    n, c = 5, 3
    houses = [1, 2, 8, 4, 9]

    print(install_router(c, houses))