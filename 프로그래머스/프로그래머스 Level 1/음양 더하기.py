def solution(absolutes, signs):
    return sum([(n if signs[i] else -n) for i, n in enumerate(absolutes)])


# 테스트 코드
print(solution([4, 7, 12], [True, False, True]))
