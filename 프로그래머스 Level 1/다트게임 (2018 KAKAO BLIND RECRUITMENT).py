def solution(dartResult):
    answer = []
    num = ''
    for i in dartResult:
        if i == '*':
            answer[-1] *= 2
            if len(answer) > 1:
                answer[-2] *= 2
        elif i == '#':
            answer[-1] *= -1
        elif i.isdigit():
            num += i
        elif i.isalpha():
            answer.append(int(num) ** {'S': 1, 'D': 2, 'T': 3}[i])
            num = ''
    return sum(answer)


# 아래는 테스트 코드
print(solution('1S2D*3T'))
print(solution('1D2S3T*'))
print(solution("1T2D3D#"))
