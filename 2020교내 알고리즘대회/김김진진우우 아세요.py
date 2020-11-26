t, n = map(int, input().strip().split())
li = []
for _ in range(t):
    li.append(input())
for li_ele in li:
    print(''.join([i * n for i in li_ele if i != ' ']))
