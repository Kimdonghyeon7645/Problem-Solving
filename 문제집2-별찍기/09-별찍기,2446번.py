m = int(input())
for i in range(m):
    print(' ' * i + '*' * ((m - i) * 2 - 1))
for i in range(2, m + 1):
    print(' ' * (m - i) + '*' * (i * 2 - 1))
