def solution(n, m):
    a, b = n, m
    while b:
        a, b = b, a % b
    return [a, n * m // a]


"""
최대공약수(gcd)는 유클리드 호제법을 사용해서,
a, b 두 수를 a, b = b, a % b 로 반복해서, b가 0이 될 때의 a값이 최대공약수고,
최소공배수(lcm)는
a, b 두 수가 있으면, a * b = 최대공약수 * 최소공배수의 공식을 이용했다.
"""
# 아래는 테스트 코드
print(solution(3, 12))
print(solution(10, 15))
