# 내장함수 안 쓴 버전
n = int(input())
sum_n = 0
for i in range(1, n+1):
    sum_n += i
print(sum_n)

# 내장함수 쓴 버전
print(sum(range(int(input()) + 1)))
