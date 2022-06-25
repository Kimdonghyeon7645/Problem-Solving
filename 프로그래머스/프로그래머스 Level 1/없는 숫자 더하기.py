# def solution(numbers):
#     return sum(set(range(10)) - set(numbers))
solution = lambda x: sum(set(range(10)) - set(x))


if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
