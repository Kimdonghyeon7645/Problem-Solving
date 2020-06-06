m = int(input())
for i in range(1, m+1):
    print('*' * i + ' ' * (m - i) * 2 + '*' * i)
for i in range(1, m):
    print('*' * (m - i) + ' ' * i * 2 + '*' * (m - i))