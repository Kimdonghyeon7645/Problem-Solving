def solution(n):
    answer = ''
    w = 1
    n -= w
    while n - (3 ** w) >= 0:
        n -= (3 ** w)
        w += 1
    while n // 3 >= 1:
        answer = str(n % 3) + answer
        n //= 3
    answer = str(n) + answer
    return answer.zfill(w).replace('2', '4').replace('1', '2').replace('0', '1')


# for i in range(1, 100):
#     print(i, '=>', solution(i))
