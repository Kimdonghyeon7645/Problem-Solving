def solution(progresses, speeds):
    dayday = [[0, 0]]
    for i, n in enumerate(progresses):
        work = (100 - n) // speeds[i]   # work : 걸리는 시간을 저장
        if (100 - n) // speeds[i] < (100 - n) / speeds[i]:  # 올림
            work += 1
        if work > dayday[-1][0]:
            dayday.append([work, 1])
        else:
            dayday[-1][1] += 1
    answer = [i[1] for i in dayday if i != [0, 0]]
    return answer


# 아래는 테스트문
progresses = [93,30,55]	
speeds = [1,30,5]
print(solution(progresses, speeds))