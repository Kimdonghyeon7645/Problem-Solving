def solution(s):
    stack = 0
    for i in s:
        if i == "(":
            stack += 1
        elif stack > 0:
            stack -= 1
        else:
            return False
    return stack == 0


# 테스트 코드
print(solution("()()"))
print(solution(")()("))
print(solution("(()("))
