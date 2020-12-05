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


# def solution(s):
#     li = list(reversed(s))
#     stack = [li.pop()]
#     while li:
#         target = li.pop()
#         if stack and target == stack[-1]:
#             del stack[-1]
#         else:
#             stack.append(target)
#         print(stack, li[::-1])
#     return 0 if stack else 1
"""
와...
딱 7분 만에 문제가 풀렸다. 내가 생각했던게 한번에 맞았다. 내가 알고리즘 수업 때 배운 방법이 맞은 것이다...
확실하게 이번 문제로 배운 것은, 나 자신에 대한 자만보다도, 알고리즘 접근 방식을 배울 필요가 있다는 것이였다. 
마치 가장 효율적이라 발견된 자료구조를 배우듯이 말이다.
"""
# TODO 알고리즘 책 읽고 정리해뵈기!


def solution(s):
    stack = []
    for ele in s:
        if stack and ele == stack[-1]:
            del stack[-1]
        else:
            stack.append(ele)
        print(stack, s[::-1])   # 출력문
    return 0 if stack else 1
# + 다른 사람의 풀이를 보니까 for 문 돌려서 하는 것이, 모든 요소를 pop() 하는 것보다 좋았던 것 같다.
# + 그리고 굳이 list(reversed()) 로 뒤집을 필요가 없었다. 괜히 시간낭비였다.
# 반영하자.


# 테스트 코드
print(solution("baabaa"))
print(solution("cdcd"))
print(solution("aa"))
