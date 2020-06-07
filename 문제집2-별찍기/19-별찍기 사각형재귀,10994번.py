li = ['*']
for i in range(1, int(input())):
    li = ['*' * (4 * i + 1)] + ['*' + ' ' * (4 * i - 1) + '*'] + ['* ' + li[i] + ' *' for i in range(len(li))] + \
         ['*' + ' ' * (4 * i - 1) + '*'] + ['*' * (4 * i + 1)]
for col in li:
    print(col)
