# 6:45 ~ 7:30, 45분동안 머리좀 싸맸다.
# 시간을 의식하고 짜다보니까 쫒기는 느낌에 코드가 최적화가 안됬다.,,
m = int(input())
li = ['*']
if m == 1:
    print(li[0])
for i in range(1, m):
    top = []
    bottom = []
    if i % 2 == 1:  # 역삼각형 뚝딱
        for index in range(len(li)):
            top.append('*' + ' ' * (2 * (len(li) - 1 - index)) + li[index] + ' ' * (2 * (len(li) - 1 - index)) + '*')
        for index in range(len(li)):
            top.append('*' + ' ' * ((len(li) - 1 - index) * 2 - 1) + '*' * bool(len(li) - 1 - index))
        li = ['*' * (len(top[0]) + 2)] + top + bottom
        if i == m-1:
            for id, col in enumerate(li):
                print(' ' * id + col)
    else:   # 삼각형 뚝딱
        for index in range(len(li)):
            top.append('*' + ' ' * (index * 2 - 1) + '*' * bool(index))
        for index in range(1, len(li)):
            bottom.append('*' + ' ' * (2 * index) + li[index] + ' ' * (2 * index) + '*')
        li = top + ['*' + li[0] + '*'] + bottom + ['*' * (len(bottom[-1]) + 2)]
        if i == m-1:
            for id, col in enumerate(li):
                print(' ' * (len(li) - id - 1) + col)
