def solution(n):
    # return sum(int(i) for i in str(n))
    return sum(map(int, str(n)))


# 아래는 테스트 코드
print(solution(1234))
