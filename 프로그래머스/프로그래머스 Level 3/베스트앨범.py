def solution(genres, plays):
    answer = []
    value_dict = dict()
    for i, jang in enumerate(genres):
        if jang in value_dict:
            value_dict[jang][0] += plays[i]
            value_dict[jang].append((i, plays[i]))
        else:
            value_dict.update({jang: [plays[i], (i, plays[i])]})
    for i in sorted(value_dict.values(), key=lambda x: -x[0]):
        li = list(sorted(i[1:], key=lambda x: (-x[1], x[0])))
        answer.append(li[0][0])
        if len(li) > 1:
            answer.append(li[1][0])
    return answer


"""
* 가장 재생시간이 많은 장르 2개가 아니라, 모든 장르에서(장르 별로) 2개씩 가져옴
* 2,15 -> 같은 재생시간 일경우, 인덱스 버전 오름차순 가져옴
"""
# 테스트 코드
print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))
print(solution(['ppap', 'wow', 'ppap'], [100, 300, 100]))
