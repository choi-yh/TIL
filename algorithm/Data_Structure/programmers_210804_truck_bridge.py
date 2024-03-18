# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length, maxlen=bridge_length)
    bridge_sum = 0

    while True:
        # if bridge_sum == 0 and len(truck_weights) == 0:
        if sum(bridge) == 0 and len(truck_weights) == 0:
            break
        # bridge_sum -= bridge.popleft()
        bridge.append(0)

        if len(truck_weights) > 0:
            cur_truck = truck_weights.popleft()

            if sum(bridge) + cur_truck <= weight:
                bridge[-1] = cur_truck
                bridge_sum += cur_truck
            else:
                truck_weights.appendleft(cur_truck)
        answer += 1

    return answer
