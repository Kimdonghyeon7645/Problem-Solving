end = []


def gogo(li, case, n):
    if len(case) >= n or not li:
        if len(case) >= n and sorted(case) not in end:
            print('=' * 20) # TEST
            end.append(sorted(case.copy()))
        case.clear()
        return 0
    for y, x in li:
        print('좌표: ', y, x, ' , 누적:', case, len(case))  # TEST
        print('지워진 값 : ', [p for p in li if p[0] == y or p[1] == x or p[1]-p[0] == x-y or p[1]+p[0] == x+y])    # TEST
        case.append([y, x])
        gogo([p for p in li if p[0] != y and p[1] != x and p[1]-p[0] != x-y and p[1]+p[0] != x+y], case, n)


def solution(n):
    li = [[i, j] for i in range(n) for j in range(n)]
    gogo(li, [], n)
    print(len(end))    # TEST
    for i in end:
        print(i)
    return len(end)


# for i in range(2, 5):
#     print(solution(i))
print(solution(5))

# [p for p in li
#          if p[0] not in sit[0] and p[1] not in sit[1] and p[1] - p[0] not in sit[2] and p[1] + p[0] not in sit[3]]:
# li = [[0] * n] + [[0] * n] + [[0] * (2 * n - 1)] + [[0] * (2 * n - 1)]
# 1 리스트: x(열), 2 리스트: y(행), 3 리스트: x-y(/모양 대각선) 4 리스트: x+y(\모양 대각선)
