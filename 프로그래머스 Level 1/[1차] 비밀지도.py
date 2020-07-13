def solution(n, arr1, arr2):
    return [''.join(['#' if i == '1' else ' ' for i in bin(a1 | a2)[2:].zfill(n)]) for a1, a2 in zip(arr1, arr2)]


# 아래는 테스트 코드
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
