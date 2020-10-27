s = 1
for k in range(3):
    s *= int(input())
for i in range(10):
    print(list(str(s)).count(str(i)))
