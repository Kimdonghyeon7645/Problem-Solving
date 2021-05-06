# def solution(numbers):
#     max_len = len(str(max(numbers)))
#     li = list(sorted(map(lambda x: str(x).ljust(max_len), numbers),
#                        key=lambda x: tuple((x[i] != '0', x[i]) for i in range(max_len)), reverse=True))
#     return ''.join([i.strip() for i in li])

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     return ''.join(sorted(numbers,
#                       key=lambda x: tuple(-int(x[i]) if len(x) > i else -1 for i in range(len(max(numbers))+1))))

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     return ''.join(sorted(numbers, key=lambda x:
#     tuple(-int(x[i]) if len(x) > i else -1 for i in range(len(max(numbers))+1))))

# 하아... 인터넷 짱짱 : https://dailyheumsi.tistory.com/102
def solution(numbers):
    return "".join(map(str, sorted([0] if all([i == 0 for i in numbers]) else numbers, key=lambda x: (str(x)*4)[:4], reverse=True)))
# 11번 문제는, [0, 0, 0] 일 때 "0"을 출력하게 해주면 된다.


# 테스트 코드
print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([40, 403]))
