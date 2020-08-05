n = int(input())
count = 0
while True:
    if n % 5 == 0:
        print(count + n // 5)
        break
    elif n < 0:
        print(-1)
        break
    n -= 3
    count += 1
