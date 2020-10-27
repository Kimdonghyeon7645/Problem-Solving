""" 기존 코드 """
# def solution(arr1, arr2):
#     answer = []
#     for i1, i2 in zip(arr1, arr2):
#         li = []
#         for i, j in zip(i1, i2):
#             li.append(i + j)
#         answer.append(li)
#     return answer


def solution(arr1, arr2):
    """ 한 줄로 개편 """
    return [[i+j for i, j in zip(i1, i2)] for i1, i2 in zip(arr1, arr2)]


# 아래는 테스트 코드
print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
