def solution(x):
    return x % sum(map(int, str(x))) == 0


# 아래는 테스트 코드
print(solution(10))
