def solution(n):
    # return list(map(int, reversed(str(n))))
    # return [int(i) for i in str(n)][::-1]
    return list(map(int, str(n)[::-1]))


# 아래는 테스트 코드
print(solution(12345))
