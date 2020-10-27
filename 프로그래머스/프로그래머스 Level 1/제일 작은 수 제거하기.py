def solution(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]


# 아래는 테스트 코드
print(solution([4,3,2,1]))
print(solution([4]))
