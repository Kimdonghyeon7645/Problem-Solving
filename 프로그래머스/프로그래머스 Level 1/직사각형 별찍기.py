a, b = map(int, input().strip().split(' '))
print(*['*'*a for i in range(b)], sep='\n')
