def solution(citations):
    for n in range(len(citations), -1, -1):
        l = len([h for h in citations if h >= n])
        if (l >= n) and (len(citations) - l <= n):
            return n


# 테스트 코드
print(solution([3, 0, 6, 1, 5]))
print(solution([31, 62]))
print(solution([0, 1, 1, 1, 1, 3, 3, 4]))
print(solution([12, 11, 10, 9, 8, 1]))
print(solution([6, 6, 6, 6, 6, 1]))
print(solution([20, 21, 22, 23]))
print(solution([4, 4, 4]))
print(solution([2, 7, 5]))
print(solution([]))
