def solution(n):
    f1, f2, f3 = 0, 0, 1
    for i in range(n-1):
        f1, f2, f3 = f2, f3, f2 + f3
    return f3 % 1234567


# 아래는 테스트 코드
print(solution(3))
print(solution(5))
