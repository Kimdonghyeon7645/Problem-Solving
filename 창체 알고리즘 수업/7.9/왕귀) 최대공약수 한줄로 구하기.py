# 유클리드 호제법으로,
def handmade_gcd(num1: int, num2: int) -> int:
    if num2 == 0:
        return num1
    return handmade_gcd(num2, num1 % num2)
# 재귀함수 코드로 위와 같이 해결할 수 있는데,

"""
좀 깔삼하게 최대공약수 해결해보자.
"""
# 1. math.gcd
import math

print(math.gcd(132, 759))   # 으악! 3줄을 차지한다!


# 2. 재귀함수 축약해 작성
def short_write_gcd(a, b): return a if b == 0 else short_write_gcd(b, a % b)


print(short_write_gcd(132, 759))    # 와... 한줄에다 자잘한 밑줄도 쳐지지 않는다니... 이건 예술이다...
