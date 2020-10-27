n = o = list(input().zfill(2))
s = 1
while True:
    n = [n[-1]] + [str(int(n[0]) + int(n[1]))[-1]]
    if n == o:
        break
    s += 1
print(s)
