# 6:45 ~ 7:30, 45분동안 머리좀 싸맸다.
# 시간을 의식하고 짜다보니까 쫒기는 느낌에 코드가 최적화가 안됬다,,,
li = ['*']
for i in range(1, int(input())):
    top = []
    bottom = []
    if i % 2 == 1:  # 역삼각형 뚝딱
        for index in range(len(li)):
            top.append('*' + ' ' * (2 * (len(li) - 1 - index)) + li[index] + ' ' * (2 * (len(li) - 1 - index)) + '*')
        for index in range(len(li)):
            top.append('*' + ' ' * ((len(li) - 1 - index) * 2 - 1) + '*' * bool(len(li) - 1 - index))
        li = ['*' * (len(top[0]) + 2)] + top + bottom
    else:   # 삼각형 뚝딱
        for index in range(len(li)):
            top.append('*' + ' ' * (index * 2 - 1) + '*' * bool(index))
        for index in range(1, len(li)):
            bottom.append('*' + ' ' * (2 * index) + li[index] + ' ' * (2 * index) + '*')
        li = top + ['*' + li[0] + '*'] + bottom + ['*' * (len(bottom[-1]) + 2)]

for id, col in enumerate(li):
    if li[0] == '*':    # 삼각형 출력
        print(' ' * (len(li) - id - 1) + col)
    else:   # 역삼각형 출력
        print(' ' * id + col)
