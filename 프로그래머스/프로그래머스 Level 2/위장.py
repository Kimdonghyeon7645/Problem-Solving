"""
조합에 관한 여러운 수식도 세우면서 정말 어렵게 접근했었는데,
사실 맨처음에 생각했던 방식이 맞았다. 왜 그때 정답이 안나와서 이렇게 헤메는 길에 들어섰는지 모르겠다....
그래도 이 경험으로 파이썬 실행문 작성법에 대해서 배울 수 있었다.
"""
# def solution(clothes):
#     c = (lambda n, r: eval('*'.join(map(str, range(n, n-r, -1)))) // eval('*'.join(map(str, range(r, 0, -1)))))
#     _, kind = zip(*clothes)
#     table = dict(((k, kind.count(k)) for k in set(kind)))
#     answer = len(clothes)
#     for i in range(2, len(table)+1):
#         answer += c(len(clothes), i)
#         for v in [v for k, v in table.items() if v >= i]:
#             temp_i = i if v >= i else v
#             answer -= c(v, i)
#   return answer


def solution(clothes):
    _, kind = zip(*clothes)
    table = dict(((k, kind.count(k)) for k in set(kind)))
    return eval("*".join([str(i[1]+1) for i in table.items()]))-1


# 테스트 코드
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
print(solution([["1", "h"], ["2", "h"], ["3", "e"]]))
print(solution([["1", "f"], ["2", "f"], ["3", "f"]]))
print(solution([["1", "h"], ["2", "h"], ["3", "i"], ["4", "j"]]))
