def solution(a, b):
    return sum((range(a, b+1) if a < b else range(b, a+1)))


# 아래는 테스트 코드
print(solution(3, 5))
