m = int(input())
for i in range(m-1):
    print(' ' * (m - i - 1) + '*' + ' ' * (i * 2 - 1) + '*' * bool(i))
print('*' * (m * 2 - 1))
