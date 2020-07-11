def solution(s):
    return ''.join([n.upper() if i % 2 == 0 else n.lower() for l in s.split(' ') for i, n in enumerate(l + ' ')])[:-1]


print(solution("try hello world"))
print(solution("a   b  c d eF"))
print(solution("   a   b  c d eF   "))
