s = 0
for i in range(int(input())):
    li = []
    s += 1
    for c in input():
        if c not in li:
            li.append(c)
        elif c != li[-1]:
            s -= 1
            break
print(s)
