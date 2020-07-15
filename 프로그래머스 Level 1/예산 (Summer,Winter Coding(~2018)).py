def solution(d, budget):
    answer = 0
    while d:
        if budget - min(d) >= 0:
            budget -= min(d)
            d.remove(min(d))
            answer += 1
        else:
            break
    return answer


# 아래는 테스트 코드
print(solution([1, 3, 2, 5, 4], 9))
