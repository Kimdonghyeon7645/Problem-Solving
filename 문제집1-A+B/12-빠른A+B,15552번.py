import sys

i = int(sys.stdin.readline())
for j in range(i):
    w = sys.stdin.readline().rstrip()
    n, m = map(int, w.split())
    print(n + m)


# 입력시간을 input() 대신 sys.stdin.readline() 으로 사용하는 이유 : https://www.acmicpc.net/blog/view/56
