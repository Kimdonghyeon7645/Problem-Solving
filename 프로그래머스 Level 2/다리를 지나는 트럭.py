def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    while truck_weights or bridge.count(0) != len(bridge):
        print(sum(bridge), weight)
        bridge = [bridge[i] for i in range(len(bridge)) if i != 0] + ([(truck_weights.pop(0) if truck_weights else 0)] if sum([bridge[i] for i in range(len(bridge)) if i != 0]) + (truck_weights[0] if truck_weights else 0) <= weight else [0])
        print(bridge)
        answer += 1
    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))


