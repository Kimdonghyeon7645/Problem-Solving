n, k = map(int, input().split())
result = []

qu = [i for i in range(n, 0, -1)]
while qu:
    for _ in range(k-1):
        t = qu.pop()
        qu = [t] + qu
    result.append(str(qu.pop()))
print('<' + ', '.join(result) + '>')
