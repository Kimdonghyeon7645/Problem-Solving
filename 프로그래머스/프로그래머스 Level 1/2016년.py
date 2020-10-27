def solution(a, b):
    return ("FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU")[(sum((31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)[:a-1]) + (b-1)) % 7]


# 아래는 테스트 코드
for i in range(1, 13):
    for j in range(1, 32):
        print(i, '월 ', j, '일 : ', solution(i, j), sep='')
