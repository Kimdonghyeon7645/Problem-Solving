def solution(price, money, count):
    # answer = sum(price * i for i in range(1, count+1)) - money
    # return answer if answer > 0 else 0
    return max(sum(price * i for i in range(1, count+1)) - money, 0)


if __name__ == '__main__':
    print(solution(3, 20, 4))
