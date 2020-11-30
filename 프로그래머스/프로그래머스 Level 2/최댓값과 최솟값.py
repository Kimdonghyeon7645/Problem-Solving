def solution(s):
    li = list(map(int, s.split()))
    return f"{min(li)} {max(li)}"


# 테스트 코드
print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
