def solution(n):
    for i in range(2, n):
        if n % i == 1:
            return i
# solution = lambda n: [i for i in range(2, n) if n % i == 1][0]


if __name__ == '__main__':
    print(solution(10))
    print(solution(12))
