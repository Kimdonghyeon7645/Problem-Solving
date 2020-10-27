l = []
for i in range(9):
    l.append(int(input()))
print(max(l), l.index(max(l))+1, sep='\n')
