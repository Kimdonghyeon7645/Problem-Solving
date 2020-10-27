m = int(input())
li = ['*']
for i in range(1, m):
    if i == 1:
        li += ['*'] + ['*']
    li = ['*' * (4 * i + 1)] + ['*' + ' ' * (4 * i)] + ['* ' + li[0] + '**'] + ['* ' + l + ' *' for l in li][1:] + ['*' + ' ' * (4 * i - 1) + '*'] + ['*' * (4 * i + 1)]
for i, l in enumerate(li):
    if i == 1:
        print(l.strip())
    else:
        print(l)
