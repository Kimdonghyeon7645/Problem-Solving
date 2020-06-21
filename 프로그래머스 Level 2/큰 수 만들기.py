def solution(number, k):
    for i in range(k):
        number = number.replace(min(number), '')
    return number


# dksehpa... bb(안됌... ㅠㅠ)
print(solution('1924', 2))