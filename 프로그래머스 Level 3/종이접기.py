def solution(n):
    answer = [0]
    for i in range(n-1):
        answer = answer + [0] + list(0 if i == 1 else 1 for i in reversed(answer))
    return answer


print(solution(int(input())))
# 승빈이가 어려운 문제 풀었다고 자랑하길래 나도 한번 풀어봤다. (자랑할 난이도는 아닌듯하다)
