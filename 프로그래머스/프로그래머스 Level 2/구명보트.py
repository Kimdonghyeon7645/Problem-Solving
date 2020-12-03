# def solution(people, limit):
#     answer, length = 0, len(people)
#     people.sort()
#     while length > 1:
#         if (people[0] + people[length-1]) > limit:
#             people.pop()
#             answer += 1
#             length -= 1
#         else:
#             for i in range(length-2, -1, -1):
#                 if (people[i] + people[length-1]) <= limit:
#                     people.pop(), people.pop(i)
#                     answer += 1
#                     length -= 2
#                     break
#     return answer + length
"""
테스트는 통과하는데 효율성에서 시간초과가 난다.
"""


def solution(people, limit):
    answer = 0
    left, right = 0, len(people)-1
    people.sort()
    while left <= right:
        print(people, left, right)
        if (people[left] + people[right]) <= limit:
            left += 1
        right -= 1
        answer += 1
    return answer
"""
와... 예전에 배운 퀵정렬 처럼, 왼쪽 인덱스와 오른쪽 인덱스를 증감하면서 처리했더니...
무친 효율이 나왔다... (효율성 10ms 이하...)
"""


# 테스트 코드
print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([20, 50, 50, 80], 100))
print(solution([10, 20, 90, 80], 100))
