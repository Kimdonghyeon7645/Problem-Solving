def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    answer = sum(i[0] * i[1] for i in zip(A, B))
    return answer


# 테스트 코드
print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))
