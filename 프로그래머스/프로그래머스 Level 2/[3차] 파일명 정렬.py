def solution(files):
    answer = []
    for i, file in enumerate(files):
        answer.append([])
        s = 0
        while True:
            s += 1
            print(s, file[s])
            if len(answer[i]) == 0 and file[s].isdigit():
                answer[i].append(file[:s])
                file = file[s:]
                s = 0
            elif len(answer[i]) == 1 and not file[s].isdigit():
                answer[i].extend([file[:s], file[s:]])
                break
            if s == len(file)-1:
                answer[i].append(file[:s+1])
                break
    print(answer)
    return [''.join(ele) for ele in sorted(answer, key=lambda x: (x[0].upper(), int(x[1])))]


# def solution(files):    # 위같이 정규표현식이 느리다고 쓰지 않는 것보다 지금처럼 정규 표현식을 사용하는 것이 더 빠르다.
#     import re
#
#     return [''.join(i) for i in sorted(map(lambda x: re.match("([a-zA-Z]+)([0-9]+)([^0-9]*)", x).groups(), files),
#                                        key=lambda m: (m[0].upper(), int(m[1])))]


# 테스트 코드
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["img000012345", "img1.png", "img2", "IMG02"]))
print(solution(["img000012345", "abc123defg123.jpg"]))
