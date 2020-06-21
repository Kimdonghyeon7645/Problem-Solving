s1 = []
s2 = []
for i in range(3):
    s1.append(int(input()))
for j in range(2):
    s2.append(int(input()))
print(min(s1) + min(s2) - 50)
