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


# 테스트 코드
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["img000012345", "img1.png", "img2", "IMG02"]))
