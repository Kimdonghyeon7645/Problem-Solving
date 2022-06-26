# def solution(n):
#     for i in range(1, n):
#         if i % 2 == 1:      # 홀수
#             if n % i == 0:
#                 gae = n // i
#                 if gae - (i-1)//2 < 1:
#                     continue
#                 txt = str(gae)
#                 print("==", i, "*", gae)
#                 for j in range(1, (i-1)//2+1):
#                     txt = f"{gae-j}+{txt}+{gae+j}"
#                 print(txt, "=", eval(txt))
#         else:       # 짝수
#             if (n - (i // 2)) % i == 0:
#                 gae = (n - (i // 2)) // i
#                 if gae - (i - 1) // 2 < 1:
#                     continue
#                 txt = str(gae)
#                 print("==", i, "*", gae)
#                 for j in range(1, (i-1)//2+1):
#                     txt = f"{gae-j}+{txt}+{gae+j}"
#                 txt += f"+{gae+(i-1)//2+1}"
#                 print(txt, "=", eval(txt))


# def solution(n):
#     for i in range(1, n):
#         x = n if i % 2 == 1 else n - (i // 2)
#         if x % i == 0 and x // i - (i-1) // 2 > 0:
#             nums = [x//i] if i % 2 == 1 else [x//i, x//i+1]
#             for j in range(1, (i-1)//2+1):
#                 nums = [nums[0]-1] + nums + [nums[-1]+1]
#             print("+".join(map(str, nums)), "=", sum(nums))


solution = lambda n: len([i for i in range(1, n+1)
                          if (n if i % 2 == 1 else (n - i // 2)) % i == 0
                          and (n if n % 2 == 1 else (n - i // 2)) // i - (i-1) // 2 > 0])


if __name__ == '__main__':
    print(solution(1))
    print(solution(15))
    print(solution(18))
    print(solution(36))

