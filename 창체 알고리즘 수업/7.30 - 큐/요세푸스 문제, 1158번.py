n, k = map(int, input().split())
result = []

""" 큐로 했는데 시간 초과인 경우, (2중 반복문이기도 해서..) """
# qu = [i for i in range(n, 0, -1)]
# while qu:
#     for _ in range(k-1):
#         t = qu.pop()
#         qu = [t] + qu
#     result.append(str(qu.pop()))
# print('<' + ', '.join(result) + '>')

""" 인덱스를 이용한 경우 (num = (num + k - 1) % len(qu) 가 절묘)"""
num = 0
qu = [i for i in range(1, n+1)]
for _ in range(n):
    num = (num + k - 1) % len(qu)
    result.append(str(qu.pop(num)))
print('<' + ', '.join(result) + '>')
