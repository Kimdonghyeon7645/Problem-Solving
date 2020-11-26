n = int(input())
cnt = n
yeak = []
for i in range(2, n):
    if n % i == 0:
        yeak.append(i)

for i in range(1, n+1):
    for j in yeak:
        if i % j == 0:
            cnt -= 1
print(cnt)
