for i in range(int(input())):
    n, w = input().split()
    print(*[i*int(n) for i in w], sep='')
