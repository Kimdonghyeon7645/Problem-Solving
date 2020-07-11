def solution(s):
    return ''.join([n.upper() if i % 2 == 0 else n.lower() for l in s.split(' ') for i, n in enumerate(l + ' ')])[:-1]


# 아래는 테스트 코드
print(solution("try hello world"))
print(solution("a   b  c d eF"))    # 여러개의 공백을 처리해 줄 수 있는지
print(solution("   a   b  c d eF   "))      # 앞, 뒤의 여러개 공백을 처리해 줄 수 있는지
