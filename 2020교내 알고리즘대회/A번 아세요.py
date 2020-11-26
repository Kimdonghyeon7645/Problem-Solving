input()
dic = {}
in_li = input().split()
for i in in_li:
    if i in dic:
        dic[i] += 1
    else:
        dic.update({i: 1})
result = sorted(dic.items(), key=lambda x: -x[1])
if len(result) > 1 and result[0][1] == result[1][1]:
    print("So Easy")
else:
    print(result[0][0])
    print(*[i+1 for i in range(len(in_li)) if in_li[i] == result[0][0]], sep=' ')
