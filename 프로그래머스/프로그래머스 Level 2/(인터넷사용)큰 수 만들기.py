def solution(number, k):
    stack = [number[0]]
    for n in number[1:]:
        while stack and n > stack[-1] and k > 0:
            stack.pop()
        stack.append(n)
    if k > 0:
        stack = stack[:-k]
    return stack


# 테스트 코드
print(solution('1924', 2))
print(solution('1231234', 3))
print(solution("4177252841", 4))
print(solution("99991", 3))
print(solution("999", 2))
