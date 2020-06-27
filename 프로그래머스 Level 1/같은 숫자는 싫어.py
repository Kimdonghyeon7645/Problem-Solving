def solution(arr):
    return [arr[0]] + [arr[i] for i in range(1, len(arr)) if arr[i-1] != arr[i]]


# 아래는 예제 코드
print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))
