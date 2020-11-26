n, c = int(input()), int(input())
for i in range(1, 500):
    if i**c == n:
        print(i)
        break
