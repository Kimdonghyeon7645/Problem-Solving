# def solution(nums):
#     choice_num_li = [[str(num) for num in nums], [], []]
#     for i in range(2):
#         for _ in range(len(choice_num_li[i])):
#             target = choice_num_li[i].pop()
#             choice_num_li[i+1].extend(target + str(num) for num in nums if str(num) not in target)
#     made_num_li = [sum(map(int, num)) for num in list(''.join(sorted(num)) for num in choice_num_li[-1])]
#     answer = len(made_num_li)
#     for num in made_num_li:
#         for i in range(2, int(num ** 1/2)+1):
#             if num % i == 0:
#                 answer -= 1
#                 break
#     return answer


# 숫자가 한자리 수만 있는 것이 아니다! 아참!
# def solution(nums):
#     choice_num_li = [[[num] for num in nums], [], []]
#     for i in range(2):
#         for target in choice_num_li[i]:
#             choice_num_li[i+1].extend(list(sorted(target + [num])) for num in nums if num not in target)
#     # print(choice_num_li[-1])
#     made_num_li = [sum(num) for num in choice_num_li[-1]]
#     # print(made_num_li)
#     answer = len(made_num_li)
#     for num in made_num_li:
#         for i in range(2, int(num ** 1/2)+1):
#             if num % i == 0:
#                 answer -= 1
#                 break
#     return answer


# 다 풀리는데 시간 초과...
# def solution(nums):
#     choice_num_li = [[[num] for num in nums], [], []]
#     for i in range(2):
#         for target in choice_num_li[i]:
#             for li in [list(sorted(target + [num])) for num in nums if num not in target]:
#                 if li not in choice_num_li[i+1]:
#                     choice_num_li[i+1].append(li)
#     made_num_li = [sum(num) for num in choice_num_li[-1]]
#     answer = len(made_num_li)
#     for num in made_num_li:
#         for i in range(2, int(num ** 1/2)+1):
#             if num % i == 0:
#                 answer -= 1
#                 break
#     return answer


def solution(nums):
    """
    아니 소수 만들기라고 해서 모든 경우의 수를 시간 효율적이게 하려고 아둥바둥 했었었다;;
    근데 걍 3중 for 문으로 해결될 일이였다...
    """
    answer = 0
    for num in [nums[i]+nums[j]+nums[k] for i in range(len(nums)-2) for j in range(i+1, len(nums)-1) for k in range(j+1, len(nums))]:
        for i in range(2, int(num ** 1/2)+1):
            if num % i == 0:
                answer -= 1
                break
        answer += 1
    return answer


# 테스트 코드
print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
print(solution([1, 2, 3, 4, 5, 7, 8]))
