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

""" 유클리드 호제법

예를 들어서, 380과 100의 최대공약수를 구한다면,
380 = 100*3 + 80 이므로,
100 = 80*1 + 20,
80 = 20*4 + 0 
이 되는데, 여기서 나머지가 0이 되면, 그때의 수 20이 최대 공약수가 된다.
"""