def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]


# 아래는 테스트 코드
print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))
