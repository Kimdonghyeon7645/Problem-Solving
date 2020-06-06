# 시에르핀스키 삼각형
# 10번 별찍기 문제의 숏코딩 풀이를 보고 활용해서, 총 50분 걸려, 8줄의 심플한 코드를 만들었다. 난이도 있다...
m = int(input())
l = ['*', '* *', '*****']
c = 1
while c * 3 < m:
    l += [str(l[c * 3 - i]) + ' ' * (i * 2 - 1) + str(l[c * 3 - i]) for i in range(c * 3, 0, -1)]
    c <<= 1
for i, n in enumerate(l):
    print(' ' * (len(l) - 1 - i) + n + ' ' * (len(l) - 1 - i))
