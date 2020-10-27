def solution(n):
    three_num = []
    while n > 0:    # 10진수 -> n진수 변환
        three_num.append(n % 3)
        n //= 3
    three_num.reverse()     # 3진수 뒤집기
    return sum(map(lambda i: i[1] * (3 ** i[0]), enumerate(three_num)))   # 한줄로 n진수 -> 10진수 변환


# 테스트 코드
print(solution(45))
print(solution(125))
