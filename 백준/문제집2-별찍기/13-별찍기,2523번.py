m = int(input())
for i in range(m-1, 0, -1):
    print('*' * (m - i))
for i in range(0, m+1):
    print('*' * (m - i))
