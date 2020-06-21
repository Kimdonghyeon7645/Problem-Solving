sum = 0
for i in range(5):
    t = int(input())
    sum = sum + (t if t > 40 else 40)
print(sum // 5)
