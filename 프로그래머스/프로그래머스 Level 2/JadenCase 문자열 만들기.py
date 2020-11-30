def solution(s):
    return ' '.join(i[0].upper()+i[1:].lower() if i != '' else '' for i in s.split(' '))


# 테스트 코드
print(solution("3people unFollowed me"))
print(solution("for the last week"))
print(solution("hello my  friend"))
print(solution("hello my    friend"))
