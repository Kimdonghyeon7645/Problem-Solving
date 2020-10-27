def hansu(n):
    chari = 0
    for id in range(len(str(n))-1):
        if id == 0:
            chari = int(str(n)[id]) - int(str(n)[id+1])
        elif chari != int(str(n)[id]) - int(str(n)[id+1]):
            return 0
    return 1


s = 0
for i in range(1, int(input()) + 1):
    s += hansu(i)
print(s)
