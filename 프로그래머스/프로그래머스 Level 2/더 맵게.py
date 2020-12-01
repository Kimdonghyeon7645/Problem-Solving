import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        answer += 1
        if len(scoville) < 2:
            return -1
        first, second = heapq.heappop(scoville), heapq.heappop(scoville) * 2
        if first == second == 0:
            return -1
        heapq.heappush(scoville, first + second)
    return answer


# 테스트 코드
print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([0, 0, 1], 3))
print(solution([0, 0, 1], 0))
print(solution([0, 1, 1], 5))
print(solution([1], 6))
