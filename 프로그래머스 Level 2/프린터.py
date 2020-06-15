def solution(priorities, location):
    m = len(priorities)
    while True:
        if priorities[0] < max(priorities):
            priorities.append(priorities.pop(0))
        else:
            priorities.pop(0)
            if location == 0:
                break
        location = location - 1 if location >= 1 else len(priorities) - 1
    return m - len(priorities)


# 아래는 테스트 코드
print(solution([2, 1, 3, 2], 0))
