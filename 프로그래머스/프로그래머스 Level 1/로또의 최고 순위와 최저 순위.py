def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    matching = len(set(win_nums) & set(lottos))
    return [rank[matching + lottos.count(0)], rank[matching]]


# 테스트 코드
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
