def solution(works, n):
    works.sort(reverse=True)
    for i in range(1, len(works)):
        diff = works[i-1] - works[i]
        if diff * i < n:
            n -= diff * i
        else:
            minus_diff = n // i
            more_minus = n % i
            return sum((works[i-1] - minus_diff - (1 if more_minus > j else 0)) ** 2 for j in range(i)) + sum(j ** 2 for j in works[i:])
    if works[-1] * len(works) > n:
        minus_diff = n // len(works)
        more_minus = n % len(works)
        return sum((works[-1] - minus_diff - (1 if more_minus > j else 0)) ** 2 for j in range(len(works)))
    return 0


if __name__ == '__main__':
    print(solution([4, 3, 3], 4))
    print(solution([2, 1, 2], 1))
    print(solution([1, 1], 3))
    print(solution([7, 5, 4, 9, 15, 3, 2, 13, 31], 89))
