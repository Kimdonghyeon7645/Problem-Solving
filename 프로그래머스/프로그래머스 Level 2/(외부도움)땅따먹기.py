def solution(land):
    for row in range(len(land) - 2, -1, -1):
        # print(land[row], end='->')
        for col in range(4):
            land[row][col] += max([land[row + 1][i] for i in range(4) if i != col])
    # print(land[row])
    return max(land[0])


# 테스트 코드
print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
print(solution([[1, 2, 3, 5], [5, 6, 7, 100], [4, 3, 2, 1]]))
print(solution([[99, 98, 97, 95], [100, 3, 2, 1]]))
