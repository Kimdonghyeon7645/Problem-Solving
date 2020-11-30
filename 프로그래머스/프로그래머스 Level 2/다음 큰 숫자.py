def solution(n):
    one_cnt = f"{n:b}".count("1")
    while True:
        n += 1
        if f"{n:b}".count("1") == one_cnt:
            return n


# 테스트 코드
print(solution(78))
