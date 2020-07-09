# 반복문
n, m = map(int, input().split())
n, m = (n, m) if n > m else (m, n)
while m != 0:
    n, m = m, n % m
print(n)


# 재귀함수
def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(n, m))
