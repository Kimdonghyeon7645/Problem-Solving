def solution(arr1, arr2):
    answer = []
    for i, row in enumerate(arr1):
        answer.append([])
        for col in range(len(arr2[0])):
            answer[i].append(sum(i[0]*i[1] for i in zip(row, [i[col] for i in arr2])))
    return answer


# 테스트 코드
print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4], [2, 4], [3, 1]]))    # 런타임 에러나는지 체크!
