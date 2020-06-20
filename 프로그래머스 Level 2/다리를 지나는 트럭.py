def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    bridge_in = bridge_sum = 0
    while truck_weights or bridge_in:
        bridge_in -= bool(bridge[0])
        bridge_sum -= bridge[0]
        front = bridge[1:]
        if truck_weights:
            if bridge_sum + truck_weights[0] <= weight:
                bridge = front + [truck_weights.pop(0)]
                bridge_sum += bridge[-1]
                bridge_in += 1
            else:
                bridge = front + [0]
        else:
            bridge = front + [0]
        print(bridge, bridge_in)
        answer += 1
    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))


