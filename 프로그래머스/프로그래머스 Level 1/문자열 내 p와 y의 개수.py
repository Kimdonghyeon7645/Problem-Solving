def solution(s):
    return (s.count('p') + s.count('P')) == (s.count('y') + s.count('Y'))
    # return (s.lower().count('p')) == (s.lower().count('y'))   # 이런 코드가 더 괜찮을 듯 하다.


print(solution("pPoooyY"))
print(solution("Pyy"))
