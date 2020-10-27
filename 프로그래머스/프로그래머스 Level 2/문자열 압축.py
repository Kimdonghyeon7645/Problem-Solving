"""
문자열 압축이라는 것이,
일정한 개수로만 딱떨어지게 짤라야 된다는 것을 한참 뒤에 이해했다;;
"""


def solution(s):
    answer = 1000
    for i in range(1, len(s)//2+2):
        li = [[s[:i], 1]]
        for j in range(i, len(s), i):
            if li[-1][0] == s[j:j+i]:
                li[-1][1] += 1
            else:
                li.append([s[j:j+i], 1])
        n = sum([len(i[0])+(len(str(i[1])) if i[1] != 1 else 0) for i in li])
        if answer > n:
            answer = n
    return answer



# 테스트 코드
print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("xxxxxxxxxxyy"))  # 고려할 점 : 개수가 10개 이상이 되면, 숫자부분의 길이가 더이상 1이 아니게 됨, 이부분의 처리 필요
