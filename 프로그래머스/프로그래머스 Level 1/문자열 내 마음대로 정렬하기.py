# 영 좋지 않은 효율의 함수
# def solution(strings, n):
#     li = [[] for i in range(ord('a'), ord('z')+1)]
#     for yo in strings:
#         li[ord(yo[n]) - 97].append(yo)
#     for i in range(ord('a') - 97, ord('z') - 96):
#         li[i].sort()
#     return [x for y in li if y != [] for x in y]


def solution(strings, n):
    return sorted(sorted(strings), key=lambda strings: strings[n])


# 아래는 테스트 코드
print(solution(['sun', 'bed', 'car'], 1))
print(solution(['abce', 'abcd', 'cdx'], 2))
