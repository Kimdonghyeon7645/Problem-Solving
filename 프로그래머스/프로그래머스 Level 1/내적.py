def solution(a, b):
    return sum(a[i]*b[i] for i in range(len(a)))


# 테스트 코드
print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
