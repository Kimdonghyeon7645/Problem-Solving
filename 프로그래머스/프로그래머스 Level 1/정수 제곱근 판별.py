# from math import sqrt


def solution(n):
    # return int((sqrt(n)+1)**2) if sqrt(n) > 0 and str(sqrt(n))[-1] == '0' else -1
    # 아! 파이썬에서 math.sqrt 함수를 쓰지 않고, 제곱근을 구할 수 있는 방법이 있다! 바로 **(1/2) = 1/2를 제곱해주는 것이다.
    return int((n**(1/2) + 1) ** 2) if n**(1/2) > 0 and str(n**(1/2))[-1] == '0' else -1


print(solution(121))
print(solution(3))
