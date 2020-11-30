def solution(s):
    loop_cnt, zero_cnt = 0, 0
    while s != "1":
        loop_cnt += 1
        zero_cnt += s.count("0")
        s = f"{s.count('1'):b}"
    return [loop_cnt, zero_cnt]


# 테스트 코드
print(solution("110010101001"))
