def solution(brown, yellow):
    b = (brown-8)//2 + 2
    for i in range(1, b//2+1):
        if i * (b-i) == yellow:
            return [b-i+2, i+2]


# 테스트 코드
print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
