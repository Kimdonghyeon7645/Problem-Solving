# def solution(left, right):
#     answer = 0
#     for num in range(left, right+1):
#         yag_su = sum([2 for i in range(1, int(num**(1/2))+1) if num % i == 0]) - (1 if num % num**(1/2) == 0 else 0)
#         answer += num * (1 if yag_su % 2 == 0 else -1)
#     return answer
# solution = lambda l, r: sum(n * (1 if (sum([2 for i in range(1, int(n**(1/2))+1) if n % i == 0]) - (1 if n % n**(1/2) == 0 else 0)) % 2 == 0 else -1) for n in range(l, r+1))

# 약수를 (1~수의 루트)까지 계산하면 항상 약수의 개수는 짝수, 만약 수의 루트가 약수면(=제곱수) 약수의 개수는 항상 홀수
solution = lambda l, r: sum(n * (1 if n % n**(1/2) else -1) for n in range(l, r+1))


if __name__ == '__main__':
    print(solution(13, 17))
    print(solution(24, 27))
