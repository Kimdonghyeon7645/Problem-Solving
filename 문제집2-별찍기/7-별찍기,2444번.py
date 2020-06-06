m = int(input())
for i in range(m-1):
    print(" " * (m - i - 1) + "*" * (1 + i*2))
for i in range(m):
    print(" " * i + "*" * ((m - i)*2 - 1))
