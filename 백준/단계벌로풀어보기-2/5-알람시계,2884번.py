a, b = map(int, input().split())
b -= 45
if b < 0:
    b = 60 + b
    a -= 1
if a < 0:
    a = 23
print(a, b)