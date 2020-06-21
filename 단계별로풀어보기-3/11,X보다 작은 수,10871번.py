x = int(input().split()[1])
print(*(i for i in map(int, input().split()) if i < x))
# for i in map(int, input().split()):
#     if i < x: print(i, end=' ')
