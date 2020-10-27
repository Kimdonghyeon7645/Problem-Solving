m = int(input())
for i in range(m*2):
    for j in range(m):
        print(('*' if j % 2 == 0 else ' ') if i % 2 == 0 else (' ' if j % 2 == 0 else '*'), end='')
    print()
