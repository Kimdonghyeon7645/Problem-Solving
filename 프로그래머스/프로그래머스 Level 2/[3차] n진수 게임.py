def solution(n, t, m, p):
    i, answer = [0], []
    while len(answer) < p-1 + t*m:
        answer.extend(list(map(str, reversed(i))))
        i[0] += 1
        for index, ele in enumerate(i):
            if ele >= n:
                if i[-1]:
                    i.append(0)
                i[index], i[index+1] = ele % n, ele//n + i[index+1]
    return answer, ''.join([(i if int(i) < 10 else chr(int(i) + 55)) for i in answer[p-1:(p-1+t*m):m]])


# 테스트 코드
# print(solution(2, 4, 2, 1))
# print(solution(16, 16, 2, 1))
# print(solution(16, 16, 2, 2))
print(solution(8, 8, 2, 2))
print(solution(16, 1000, 100, 1))
