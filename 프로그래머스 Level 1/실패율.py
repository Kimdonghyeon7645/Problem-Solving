def solution(N, stages):
    answer = [0] * N
    for i in range(1, N+1):
            answer[i-1] = [i, len([j for j in stages if j == i]) / len([j for j in stages if j > i or j == N])]
    return [i[0] for i in sorted(answer, key=lambda x: (-x[1], x[0]))]


# 아래는 테스트 코드
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
