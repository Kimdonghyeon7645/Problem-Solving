def solution(n, lost, reserve):
    for pp in lost.copy():
        if pp in reserve:
            lost.remove(pp)
            reserve.remove(pp)
    for people in lost.copy():
        for mazin in reserve:
            if mazin+1 == people or mazin-1 == people:
                lost.remove(people)
                reserve.remove(mazin)
                break
    return n - len(lost)


# 아래는 테스트 코드
print(solution(5, [2, 4], [1, 3, 5]))
