def solution(n):
    answer = [i for i in range(2, n+1)]
    for i in answer.copy():
        if answer[i-2] != 0:
            for j in range(2, n//i + 1):
                answer[j*i-2] = 0
    return [i for i in answer if i != 0]


# 아래는 테스트 코드
for i in range(1, 1000):
    res = solution(i)
    print(f"{i} (총 소수의 개수 - {len(res)} :", res)
