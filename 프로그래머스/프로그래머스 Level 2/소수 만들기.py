def solution(nums):
    choice_num_li = [[str(num) for num in nums], [], []]
    for i in range(2):
        for _ in range(len(choice_num_li[i])):
            target = choice_num_li[i].pop()
            choice_num_li[i+1].extend(target + str(num) for num in nums if str(num) not in target)
    made_num_li = [sum(map(int, num)) for num in set(''.join(sorted(num)) for num in choice_num_li[-1])]
    answer = len(made_num_li)
    for num in made_num_li:
        for i in range(2, int(num ** 1/2)+1):
            if num % i == 0:
                answer -= 1
                break
    return answer


# 테스트 코드
print(solution([1, 2, 3, 4]))
print(solution([1, 2, 3, 4]))
print(solution([1, 2, 3, 4, 5, 7, 8]))
