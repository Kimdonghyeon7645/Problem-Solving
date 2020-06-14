# 미완성
def solution(n):
    i = j = 1
    n -= 1
    answer = str(n).replace('2', '4').replace('1', '2').replace('0', '1')
    if n / 3 >= 1:
        while n / (3 ** i) >= 1:
            n -= (3 ** i)
            i += 1
        answer = ['0'] * i
        while n // 3 >= 3:
            answer[len(answer) - j] = str(n % 3)
            n //= 3
            j += 1
            if n // 3 > 3:
                break
        answer[len(answer) - j] = str(n % 3)
        j += 1
        if n // 3 > 0:
            answer[len(answer) - j] = str(n // 3)
        answer = ''.join(answer).replace('2', '4').replace('1', '2').replace('0', '1')
    return answer


for i in range(1, 100):
    print(i, '=>', solution(i))