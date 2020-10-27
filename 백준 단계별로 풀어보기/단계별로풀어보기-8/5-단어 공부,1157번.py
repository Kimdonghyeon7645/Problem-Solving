li = [0] * 26
for i in input():
    li[ord(i)-97 if ord(i) > 96 else ord(i)-65] += 1
print('?' if str(li).count(str(max(li))) > 1 else chr(li.index(max(li)) + 65))
