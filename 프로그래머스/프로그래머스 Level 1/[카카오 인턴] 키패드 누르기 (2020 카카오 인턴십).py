# def solution(numbers, hand):
#     answer = ''
#     kpad = [[1, 4, 7, '*'], [2, 5, 8, 0], [3, 6, 9, '#']]
#     l = [0, kpad[0].index('*')]
#     r = [2, kpad[2].index('#')]
#
#     for n in numbers:
#         if n in kpad[0]:    # 누를 번호 == [1, 4, 7]
#             l = [0, kpad[0].index(n)]
#             answer += 'L'
#
#         elif n in kpad[1]:  # 누를 번호 == [2, 5, 8, 0]
#             kpad_n = kpad[1].index(n)
#             l_load = 1-l[0] + (kpad_n - l[1] if kpad_n > l[1] else l[1] - kpad_n)
#             r_load = r[0]-1 + (kpad_n - r[1] if kpad_n > r[1] else r[1] - kpad_n)
#             if l_load < r_load:     # 왼손이 오른손보다 빠를 때
#                 l = [1, kpad_n]
#                 answer += 'L'
#             elif r_load < l_load:     # 오른손이 왼손보다 빠를 때
#                 r = [1, kpad_n]
#                 answer += 'R'
#             elif r_load == l_load:     # 왼손과 오른손이 동일한 거리일 때
#                 if hand == 'right':     # 오른손 잡이면
#                     r = [1, kpad_n]
#                     answer += 'R'
#                 else:       # 왼손 잡이면
#                     l = [1, kpad_n]
#                     answer += 'L'
#
#         elif n in kpad[2]:
#             r = [2, kpad[2].index(n)]
#             answer += 'R'
#     return answer


def solution(numbers, hand):
    answer = ''
    kpad = [[1, 4, 7, '*'], [2, 5, 8, 0], [3, 6, 9, '#']]
    l = [0, kpad[0].index('*')]
    r = [2, kpad[2].index('#')]

    for n in numbers:
        if n in kpad[0]:    # 누를 번호 == [1, 4, 7]
            l = [0, kpad[0].index(n)]
            answer += 'L'

        elif n in kpad[1]:  # 누를 번호 == [2, 5, 8, 0]
            kpad_n = kpad[1].index(n)
            l_load = 1-l[0] + (kpad_n - l[1] if kpad_n > l[1] else l[1] - kpad_n)
            r_load = r[0]-1 + (kpad_n - r[1] if kpad_n > r[1] else r[1] - kpad_n)
            if l_load < r_load or (r_load == l_load and hand == 'left'):
                # 왼손이 오른손보다 빠를 때 <OR> 왼손과 오른손이 동일한 거리일 때 왼손 잡이면
                l = [1, kpad_n]
                answer += 'L'
            elif r_load < l_load or (r_load == l_load and hand == 'right'):
                # 오른손이 왼손보다 빠를 때 <OR> 왼손과 오른손이 동일한 거리일 때 오른손 잡이면
                r = [1, kpad_n]
                answer += 'R'

        elif n in kpad[2]:  # 누를번호 == [3, 6, 9]
            r = [2, kpad[2].index(n)]
            answer += 'R'
    return answer


# 아래는 테스트 코드
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
