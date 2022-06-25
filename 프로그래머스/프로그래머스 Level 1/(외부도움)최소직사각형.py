# 실패...
# def solution(sizes):
#     answer = sizes[0]
#     for size in sizes:
#         x, y = sorted(((0, 1), (1, 0)), key=lambda i: abs(max(size[i[0]] - answer[0], 0) - max(size[i[0]] - answer[1], 0)))[1]
#         answer = max(answer[0], size[x]), max(answer[1], size[y])
#     return answer[0] * answer[1]

# def solution(sizes):
#     l = [(max(x, y), min(x, y)) for x, y in sizes]
#     return max(i[0] for i in l) * max(i[1] for i in l)

# solution = lambda s: max(i for i in (max(x, y) for x, y in s)) * max(i for i in (min(x, y) for x, y in s))
solution = lambda s: max(max(x) for x in s) * max(min(x) for x in s)


if __name__ == '__main__':
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
    print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
    print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
