def solution(numbers):
    max_len = len(str(max(numbers)))
    li = list(sorted(map(lambda x: str(x).ljust(max_len), numbers),
                       key=lambda x: tuple((x[i] != '0', x[i]) for i in range(max_len)), reverse=True))
    return ''.join([i.strip() for i in li])


# 테스트 코드
print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
