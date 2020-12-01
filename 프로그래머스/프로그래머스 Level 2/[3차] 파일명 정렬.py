# def solution(files):
#     answer = []
#     for i, file in enumerate(files):
#         answer.append([])
#         s = 0
#         while True:
#             s += 1
#             print(s, file[s])
#             if len(answer[i]) == 0 and file[s].isdigit():
#                 answer[i].append(file[:s])
#                 file = file[s:]
#                 s = 0
#             elif len(answer[i]) == 1 and not file[s].isdigit():
#                 answer[i].extend([file[:s], file[s:]])
#                 break
#             if s == len(file)-1:
#                 answer[i].append(file[:s+1])
#                 break
#     print(answer)
#     return [''.join(ele) for ele in sorted(answer, key=lambda x: (x[0].upper(), int(x[1])))]

def solution(files):
    import re

    return [''.join(i) for i in sorted(map(lambda x: re.match(r"([^\d]+)([\d]+)([^\n]*)", x).groups(), files), key=lambda m: (m[0].upper(), int(m[1])))]
"""
정규표현식, 느린줄만 알았지만, 이런 경우에선 정규표현식이 2~3배 더 효율이 좋았다.
그리고, 본의아니게 한줄 코딩할 정도로 정규표현식은 강력했다...
"""


# 테스트 코드
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
print(solution(["img000012345", "img1.png", "img2", "IMG02"]))
print(solution(["img000012345", "abc123defg123.jpg"]))
