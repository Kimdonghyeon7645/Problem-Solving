# 반복문
n1, n2 = map(int, input().split())
n1, n2 = (n1, n2) if n1 > n2 else (n2, n1)
while n2 != 0:
    n1, n2 = n2, n1 % n2
print(n1)


# 재귀함수
def gcd(num1: int, num2: int) -> int:
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)


print(gcd(n1, n2))
"""
유클리드 
"""