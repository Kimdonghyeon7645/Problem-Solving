# def solution(s):
#     li, length, i = list(s), len(s), 1
#     while length > i and length:
#         print(li, i, length)
#         if li[i] == li[i-1]:
#             length -= 2
#             i -= 1
#             del li[i]
#             del li[i]
#         else:
#             i += 1
#     return 0 if length else 1
"""
이제는 말할 수 있다. 위와 같이 짠 코드는 매우 구리다.
del 은 시간복잡도를 많이 잡아먹으며, 이렇게 코드를 짜는 중에도, pop()으로 스텍처럼 문제를 푸는 방법이 들었다.
그 방법대로 아래와 같이 코드를 짜봤다.
"""


def solution(s):
    pass


# 테스트 코드
print(solution("baabaa"))
print(solution("cdcd"))
print(solution("aa"))
