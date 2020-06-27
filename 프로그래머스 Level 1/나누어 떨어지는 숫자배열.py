def solution(arr, divisor):
    n = sorted([i for i in arr if i % divisor == 0])
    return n if n else [-1]


# 아래는 테스트 코드
print([5, 9, 7, 10], 5)
print([2, 36, 1, 3], 1)
print([3, 2, 6], 10)
