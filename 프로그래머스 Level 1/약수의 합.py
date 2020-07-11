from math import sqrt


def solution(n):
    return [j for i in range(1, int(sqrt(n)+1)) if n % i == 0 for j in {i, n//i}]


"""
"""
# 테스트 코드
for i in range(100):
    res = solution(i)
    print(f"{i}의 약수 총합 : {sum(res)}, 총 개수 : {len(res)}, 약수 : {sorted(res)}")
