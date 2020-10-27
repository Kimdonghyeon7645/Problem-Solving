def solution1(n):   # 어렵게 생각한 풀이
    x = n if n % 2 == 0 else n - 1
    print('수박' * (x // 2) + '수' * (n - x))


def solution2(n):   # 그럴 필요 없다는 것을 깨달은 풀이
    return '수박'*(n//2) + '수'*(n % 2)


def solution3(n):   # 놀란 풀이
    return ('수박'*n)[:n]


# 아래는 테스트 코드
print(solution1(5))
print(solution2(5))
print(solution3(5))
