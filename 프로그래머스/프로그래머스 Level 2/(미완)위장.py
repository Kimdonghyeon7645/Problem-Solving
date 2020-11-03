def c(n, r):
    sum(range(n, n-r-1, -1)) // sum(i for i in range(r, 0, -1))

def solution(clothes):
    answer = dict()
    for v, k in clothes:
        answer[k].append(v) if k in answer else answer.update({k: [v]})
    print(answer, len(answer))
    for i in range(len(answer.keys())):


    return sum([len(v)+1 for v in answer.values()]) - (0 if len(answer)-1 else 1)


# 테스트 코드
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
print(solution([["1", "a"], ["1", "b"], ["1", "c"], ["1", "d"], ["1", "e"], ["1", "f"],
                ["1", "g"], ["1", "h"], ["1", "i"], ["1", "j"], ["1", "k"], ["1", "l"]]))