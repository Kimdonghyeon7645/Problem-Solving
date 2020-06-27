def solution(answers):
    connect = [0, 0, 0]
    check = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i, n in enumerate(answers):
        for j in range(3):
            if check[j][i % len(check[j])] == n:
                connect[j] += 1
    return [i+1 for i, n in enumerate(connect) if n == max(connect)]


# 아래는 테스트 코드
print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
