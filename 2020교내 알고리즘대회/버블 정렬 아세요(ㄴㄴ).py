input()
cnt = 0
li = input().split()
for i in range(len(li)-1):
    for j in range(len(li)-i-1):
        if li[j] > li[j+1]:
            cnt += 1
            li[j], li[j+1] = li[j+1], li[j]
print(cnt)
