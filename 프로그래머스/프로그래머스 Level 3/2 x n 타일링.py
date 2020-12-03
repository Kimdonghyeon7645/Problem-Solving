# def solution(n):
#     return (sum(map(lambda x: n-x, range(1, n+1, 2))) + 1) % 1000000007
def solution(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = a+b, a
    return a % 1000000007
"""
2 x n 타일링은 알고보니 DP 문제였다.
그리고 이번 케이스에서는 피보나치 수열과 같았다...
"""


# 테스트 코드
for i in range(1, 100):
    print(solution(i))
