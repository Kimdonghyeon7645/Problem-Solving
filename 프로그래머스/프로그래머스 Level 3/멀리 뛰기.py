# def solution(n):
#     from functools import reduce
#
#     answer = 1
#     for i in range(n - n//2, n):            # print(f"{i}C{n-i}")
#         answer += reduce(lambda cnt, ele: cnt * ele, list(range(i, 2*i-n, -1)), 1) // (n-i) % 1234567
#     return answer
"""
reduce 함수를 사용한 조합으로 문제를 풀었더니 실패가 난다.
예전의 '2 x n 타일링' 문제를 생각하여, DP 로 문제를 해결하자.
"""


def solution(n):
    a, b = 1, 1
    for _ in range(1, n):
        a, b = b, a+b
    return b % 1234567
    # 1234567로 나눠주라는 조건을 잊지말자


# 테스트 코드
print(solution(4))
print(solution(3))
print(solution(2000))
