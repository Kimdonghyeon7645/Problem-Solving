from math import gcd


def solution(arr):
    answer = arr[0]
    for i in arr[1:]:
        answer = answer * i // gcd(answer, i)
    return answer


# 테스트 코드
print(solution([2, 6, 8, 14]))
