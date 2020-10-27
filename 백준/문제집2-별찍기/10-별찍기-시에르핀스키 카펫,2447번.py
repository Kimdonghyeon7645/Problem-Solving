# 재귀함수를 이용한 재귀 패턴을 가지는 사각형 만들기...
# 시에르핀스키 카펫을 만드는 프로그램인데, 오랜만에 꽤 여러운 문제를 풀어본듯 했다.
# 고민한 시간 : 1~2시간? (중간에 빠진 버그를 찼는게 더 어려웠다.)
li = []
m = int(input())
for m_i in range(m):
    ll = []
    for j in range(m):
        ll.append("*")
    li.append(ll)


def hole(n, r, c):  # c 은 행, r 은 열
    piece = n // 3
    for y in range(c + piece * 1, c + piece * 2):
        for x in range(r + piece * 1, r + piece * 2):
            li[y][x] = ' '
    if piece > 1:
        for i in range(3):
            for j in range(3):
                # print('hole 호출!', piece, piece * i, piece * j)
                hole(piece, r + piece * i, c + piece * j)


hole(m, 0, 0)
for i in li:
    for j in i:
        # print(j, end=' ')
        print(j, end='')
    print()
