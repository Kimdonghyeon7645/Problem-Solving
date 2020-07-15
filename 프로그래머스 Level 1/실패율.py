def solution(N, stages):
    answer = [[0, 0] for i in range(N+1)]
    for i in stages:
        for j in range(0, i-1):
            answer[j][1] += 1
        answer[i-1][1] += 1
        answer[i-1][0] += 1
    answer.pop()
    answer = [[i+1, y[0] / y[1]] if y[1] else [i+1, 0] for i, y in enumerate(answer)]
    return [i[0] for i in sorted(answer, key=lambda x: (-x[1], x[0]))]


""" 최적화가 좋지는 않지만, 해결은 겨우 됬다! (다음엔 좀 더 최적화 해보기로..) """
# 아래는 테스트 코드
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
