def solution(nums):
    return len(set(nums)) if len(set(nums)) < len(nums)//2 else len(nums)//2


# 테스트 코드
print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
