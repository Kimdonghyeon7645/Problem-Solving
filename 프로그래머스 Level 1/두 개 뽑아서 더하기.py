def solution(numbers):
    answer = set()
    for i, n in enumerate(numbers):
        answer.update([n + m for m in numbers[i+1:]])
    return list(sorted(answer))


# 테스트 코드
print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))