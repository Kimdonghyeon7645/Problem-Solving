import math
"""
gcd()     최대공약수
ceil()    올림
floor()   내림
"""
# def solution(w, h):   #  55.6 / 100.0 점
#     enable = 0
#     for i in range(1, h+1):
#         enable += (int(w/h * i)-1 if w/h * i == int(w/h * i) and i > 0 else int(w/h * i)) - int(w/h * (i-1)) + 1
#     return (w * h) - enable


# def solution(w, h):   # 88.9 / 100.0 점 (문제 4, 17 실패)
#     enable = 0
#     gcd_num = math.gcd(w, h)
#     f, n = max(w/h, h/w), min(w, h)
#     for i in range(0, n//gcd_num):
#         enable += math.ceil(f*(i+1)) - math.floor(f*i)
#     return (w * h) - enable * gcd_num
# 4, 17번 틀리는 이유가 부동 소수점 오차래요 ?!
# https://dojang.io/mod/page/view.php?id=2466 : 실수값 오차 잡기
# from fractions import Fraction      # 분수로 순환소수 해결하기!
#
#
# def solution(w, h):       # 88.9 / 100.0 점 (문제 45, 17 시간 초과)
#     enable = 0
#     gcd_num = math.gcd(w, h)
#     f, n = max(Fraction(f"{w}/{h}"), Fraction(f"{h}/{w}")), min(w, h)
#     for i in range(0, n//gcd_num):
#         enable += math.ceil(f*(i+1)) - math.floor(f*i)
#     return (w * h) - enable * gcd_num
def solution(w, h):
    enable = 0
    gcd_num = math.gcd(w, h)
    a, b = max(w, h), min(w, h)
    for i in range(0, b//gcd_num):
        enable += math.ceil(a*(i+1)/b) - math.floor(a*i/b)
    return (w * h) - enable * gcd_num
"""
깨달은 점 :
부동 소수점 오차를 해결할 때, 라이브러리를 사용할 수 있으며 대신 성능이 낮아질 수 있다.
간편하게 오차가 생기는 소수점 아랫 부분에서 숫자를 가지고 놀지말고, 숫자의 자릿수를 높여서 가지고 놀면 오차가 확실히 준다.
"""


print(solution(8, 12))
# f = Fraction(f"{8}/{12}")
# print(f"{(2/3) * 2:.30}", f * 2, math.ceil(f * 2))
