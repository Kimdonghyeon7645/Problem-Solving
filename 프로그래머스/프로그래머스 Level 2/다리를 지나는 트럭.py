def old_solution(bridge_length, weight, truck_weights):
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


def solution(bridge_length, weight, truck_weights):
    """다리의 상태를 저장하는 배열을 다리 길이만큼의 배열 크기로 하는 대신, 가중치로 관리"""
    answer = bridge_sum = 0
    brigde = []
    while bridge_sum or truck_weights:
        for brg in brigde:
            brg[1] += 1
        if brigde and brigde[0][1] > bridge_length:
            bridge_sum -= brigde.pop(0)[0]
        answer += 1
        if truck_weights:
            if truck_weights[0] + bridge_sum <= weight:
                brigde.append([truck_weights.pop(0), 1])
                bridge_sum += brigde[-1][0]
        print(answer, brigde, truck_weights)
    return answer


# 아래는 테스트 코드
print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))


