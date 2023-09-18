# https://www.acmicpc.net/problem/1715

import heapq

n = int(input())
cards = [int(input()) for _ in range(n)]

if n == 1:
    print(0)
else:
    answer = 0
    heapq.heapify(cards)

    while len(cards) > 1:
        first = heapq.heappop(cards)
        second = heapq.heappop(cards)
        new_card = first + second
        answer += new_card
        heapq.heappush(cards, new_card)

    print(answer)
