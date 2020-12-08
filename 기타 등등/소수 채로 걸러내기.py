maximum = int(input())
natural_su, so_su = list(range(maximum, 1, -1)), []
while natural_su:
    so_su.append(natural_su.pop())
    natural_su = [i for i in natural_su if i % so_su[-1] != 0]
print(so_su)
# 채로 걸러내는 것도 있지만 '소수 판별 제곱근'을 이용하는 것도 좋다.
