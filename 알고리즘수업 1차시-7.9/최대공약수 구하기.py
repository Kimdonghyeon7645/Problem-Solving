# n = int(input())
# m = int(input())
# s = m if n > m else n
# for i in range(1, s+1):
#     if n % i == 0 and m % i == 0:
#         print(i)

n, m = map(int, input().split())
print(*[i for i in range(1, (n if n < m else m)) if n % i == 0 and m % i == 0])
