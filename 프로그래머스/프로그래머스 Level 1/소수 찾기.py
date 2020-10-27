def solution(n):
    answer = [i for i in range(2, n+1)]
    for i in answer.copy():
        if answer[i-2] != 0:
            for j in range(2, n//i + 1):
                answer[j*i-2] = 0
    return [i for i in answer if i != 0]


"""
에라토스테네스의 체,
소수를 구하는 것의 최적의 알고리즘 이다! 
이 문제를 푸는데 너무 많은 시간을 잡아먹었지만, 이제는 확실하게 소수 문제는 이 에라토스테네스의 체를 활용할 수 있을 것이다.
"""
# 아래는 테스트 코드
for i in range(1, 1000):
    res = solution(i)
    print(f"{i} (총 소수의 개수 - {len(res)} :", res)
