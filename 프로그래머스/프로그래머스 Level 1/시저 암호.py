""" 초기 코드 """
# def solution(s, n):
#     answer = ''
#     for i in s:
#         if i == ' ':
#             answer += i
#         elif ord(i) + n > ord('z'):
#             answer += chr(ord(i)+n-26)
#         elif ord(i) >= ord('a') and ord(i) + n >= ord('a'):     # i가 소문자인데 i+n이 A 이상이 되는 경우를 고려안함;;
#             answer += chr(ord(i) + n)
#         elif ord(i) + n > ord('Z'):
#             answer += chr(ord(i)+n-26)
#         else:
#             answer += chr(ord(i) + n)
#     return answer


""" 1차 개편 """
# def solution(s, n):
#     answer = ''
#     for i in s:
#         if i.islower():
#             answer += chr((ord(i)-97+n) % 26 + 97)
#         elif i.isupper():
#             answer += chr((ord(i)-65+n) % 26 + 65)
#         else:
#             answer += i
#     return answer


def solution(s, n):
    """ 2차 개편
    한줄 코딩에 맞들리면 안되는데... 이 까지만 하자.
    """
    return ''.join([chr((ord(i)-97+n) % 26 + 97) if i.islower() else
                    (chr((ord(i)-65+n) % 26 + 65) if i.isupper() else ' ') for i in s])


# 아래는 테스트 코드
print(solution("A B", 1))
print(solution("A B", 25))
print(solution("Hello World", 25))

