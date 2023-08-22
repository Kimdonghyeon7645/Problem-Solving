def solution(k, score):
    answer = []
    hof = []
    for i in range(len(score)):
        hof.append(score[i])
        hof.sort(key=lambda x: -x)
        hof=hof[:k]
        answer.append(hof[-1])
    return answer