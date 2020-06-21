n = list(input().zfill(2))
s = 1
m = [n[-1]] + [str(int(n[0]) + int(n[1]))[-1]]
while True:
    if m == n:
        break
    m = [m[-1]] + [str(int(m[0]) + int(m[1]))[-1]]
    s += 1
print(s)
