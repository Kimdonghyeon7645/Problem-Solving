# def solution(land):
#     for row in range(len(land) - 2, -1, -1):
#         # print(land[row], end='->')
#         for col in range(4):
#             land[row][col] += max([land[row + 1][i] for i in range(4) if i != col])
#     # print(land[row])
#     return max(land[0])


def solution(land):
    for row in range(len(land)-2, -1, -1):
        for col in range(4):
            land[row][col] += max(land[row+1][:col] + land[row+1][col+1:])
    return max(land[0])
"""
위처럼 리스트 내포로 검출해주는 방식은 효율성에서 350ms,
아래처럼 리스트 슬라이싱 방식은 효율성에서 200ms가 나온다.
(은근 리스트 슬라이싱 방식이 이럴때는 좋은 효율을 가지는 것을 기억하자.)
"""


# 테스트 코드
print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
print(solution([[1, 2, 3, 5], [5, 6, 7, 100], [4, 3, 2, 1]]))
print(solution([[99, 98, 97, 95], [100, 3, 2, 1]]))
