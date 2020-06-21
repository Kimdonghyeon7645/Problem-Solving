input()
li = list(map(int, input().split()))
M = max(li)
print(sum([i/M * 100 for i in li]) / len(li))