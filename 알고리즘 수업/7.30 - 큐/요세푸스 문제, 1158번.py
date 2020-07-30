n, k = map(int, input().split())
result = []

# qu = [i for i in range(n, 0, -1)]
# while qu:
#     for _ in range(k-1):
#         t = qu.pop()
#         qu = [t].append(qu)
#     result.append(str(qu.pop()))
# print('<' + ', '.join(result) + '>')
# 위에는 큐로 짰는데 효율이...

num = 0
qu = [i for i in range(1, n+1)]
for _ in range(n):
    num += k-1
    num %= len(qu)
    result.append(str(qu.pop(num)))
print('<' + ', '.join(result) + '>')
