from math import sqrt


def solution(n):
    return [j for i in range(1, int(sqrt(n)+1)) if n % i == 0 for j in {i, n//i}]


"""
약수의 개수 구하기,
0으로 나누어 떨어지는 수를 구할 때, 
n의 약수를 1~n-1 까지 반복문으로 구할 수 있지만,
n = i * j = j * i 와 같이, i, j 만 위치만 바뀌는 규칙으로,
굳이 j까지 가지 않고, i 만으로 약수 i와 j를 구할 수 있을 것이다.

그러면 어느정도까지 반복할지가 문제인데, 결국 n의 루트를 씌운 값(n제곱근)만큼 반복해야 된다.
"""
# 테스트 코드
for i in range(100):
    res = solution(i)
    print(f"{i}의 약수 총합 : {sum(res)}, 총 개수 : {len(res)}, 약수 : {sorted(res)}")
