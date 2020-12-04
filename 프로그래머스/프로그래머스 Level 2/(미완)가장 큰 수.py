# def solution(numbers):
#     max_len = len(str(max(numbers)))
#     li = list(sorted(map(lambda x: str(x).ljust(max_len), numbers),
#                        key=lambda x: tuple((x[i] != '0', x[i]) for i in range(max_len)), reverse=True))
#     return ''.join([i.strip() for i in li])


# def solution(numbers):
#     numbers = list(map(str, numbers))
#     return ''.join(sorted(numbers,
#                       key=lambda x: tuple(-int(x[i]) if len(x) > i else -1 for i in range(len(max(numbers))+1))))


def solution(numbers):
    numbers = list(map(str, numbers))
    return ''.join(sorted(numbers, key=lambda x: tuple(-int(x[i]) if len(x) > i else -1 for i in range(len(max(numbers))+1))))


# 테스트 코드
print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([40, 403]))

# 시행착오
# print(list(sorted([(4, 0, 3), (4, 0)], key=lambda x: tuple(x[i] for i in range(len(x))))))
# print(list(sorted([(7, 0, 3), (4, 0)], key=lambda x: tuple(x[i] for i in range(len(x))))))
# print(list(map(lambda x: tuple(x[i] for i in range(len(x))), ("703", "40"))))

# li = ("403", "40")
# li = ['6', '10', '2']
# li = list(map(str, [3, 30, 32, 5, 9]))
# print(list(map(lambda x: tuple(int(x[i]) if len(x) > i else 1001 for i in range(len(max(li))+1)), li)))
# print(list(sorted(li, key=lambda x: tuple(-int(x[i]) if len(x) > i else -1 for i in range(len(max(li))+1)))))
