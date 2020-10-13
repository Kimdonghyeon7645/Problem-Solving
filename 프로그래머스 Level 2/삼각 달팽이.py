"""
def solution(n):
    answer = [[0] * (i + 1) for i in range(n)]
    y, x = -1, 0
    num = 1
    for i in range(n, 0, -1):
        y_p, x_p = [(1, 0), (0, 1), (-1, -1)][(n-i) % 3]
        for _ in range(i):
            y = y + y_p
            x = x + x_p
            answer[y][x] = num
            num += 1
    return [ele for li in answer for ele in li]     # 2차원 -> 1차원 배열로 피는 기술
"""


# 파이썬 3.8의 ':=' 활용
def solution(n):
    answer = [[0] * (i + 1) for i in range(n)]
    y, x, num = -1, 0, 1
    for i in range(n, 0, -1):
        y_p, x_p = [(1, 0), (0, 1), (-1, -1)][(n-i) % 3]
        for _ in range(i):
            answer[(y := y + y_p)][(x := x + x_p)] = (num := num + 1)
    return [ele for li in answer for ele in li]


# 테스트 코드
print(solution(4))
print(solution(5))
