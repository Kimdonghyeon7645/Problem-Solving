top = []
bottom = []

# # 삼각형
li = ['*****', '***', '*']
for index in range(len(li)):
    top.append('*' + ' ' * (index * 2 - 1) + '*' * bool(index))
for index in range(1, len(li)):
    bottom.append('*' + ' ' * (2 * index) + li[index] + ' ' * (2 * index) + '*')
li = top + ['*' + li[0] + '*'] + bottom + ['*' * (len(bottom[-1]) + 2)]
for i, col in enumerate(li):
    print(' ' * (len(li) - i - 1) + col)

# # 역삼각형
li = ['*', '* *', '*   *', '*******', '*  ***  *', '*    *    *', '*************']
for index in range(len(li)):
    top.append('*' + ' ' * (2 * (len(li) - 1 - index)) + li[index] + ' ' * (2 * (len(li) - 1 - index)) + '*')
for index in range(len(li)):
    top.append('*' + ' ' * ((len(li) - 1 - index) * 2 - 1) + '*' * bool(len(li) - 1 - index))
li = ['*' * (len(top[0]) + 2)] + top + bottom
for i, col in enumerate(li):
    print(' ' * i + col)
