def solution(s):
    return ('' if len(s) % 2 else s[len(s)//2-1]) + s[len(s)//2]


# 아래는 테스트 코드
print(solution('qwer'))
