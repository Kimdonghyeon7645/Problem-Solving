def solution(x, n):
    return [i for i in range(x, x*(n+1), x)] if x else [0] * n


# 아래는 테스트 코드
print(solution(2, 5))
print(solution(4, 3))
print(solution(-2, 3))
print(solution(0, 3))
