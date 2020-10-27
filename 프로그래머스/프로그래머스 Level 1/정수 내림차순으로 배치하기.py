def solution(n):
    return int(''.join(reversed(sorted(str(n)))))


# 아래는 테스트 코드
print(solution(118372))
