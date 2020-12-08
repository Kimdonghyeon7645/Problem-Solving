# def solution(name):
#     a_cnt_l, a_cnt_r, a_cnt_l_bool, a_cnt_r_bool = 0, 0, True, True
#     for i in range(1, len(name)):
#         a_cnt_l, a_cnt_l_bool = (a_cnt_l+1, True) if a_cnt_l_bool and name[-i] == "A" else (a_cnt_l, False)
#         a_cnt_r, a_cnt_r_bool = (a_cnt_r+1, True) if a_cnt_r_bool and name[i] == "A" else (a_cnt_r, False)
#     answer = len(name) - max(a_cnt_l, a_cnt_r) - 1
#     for i in name.replace("A", ""):
#         print(i, ord(i), ord(i) - 65, 90 - ord(i) + 1)
#         answer += min(ord(i) - 65, 90 - ord(i) + 1)
#     return answer
""" 위 경우 방향은 항상 한방향으로 정해져야 된다 생각해, 맨 처음 방향을 정하고 갔는데, 반례가 있었다. """


def solution(name):
    answer = cursor = 0
    for i in name.replace("A", ""):     # A가 아닌 놈들은 A로 만들때 얼마만큼 걸리는지 계산
        answer += min(ord(i) - 65, 90 - ord(i) + 1)
    name = ["A" if i == "A" else "F" for i in name]
    print(answer)
    name[cursor] = "A"     # 출발지(cursor)에 이미 A가 아닌 놈(=F)이 있으면 처지, 제자리에서 처리했기에 거리 더할 필요 X
    while "F" in name:     # A가 아닌 놈(=F)들이 있을때까지 A를 처치하면서 움직인 거리를 계산
        # name[cursor-1::-1]+name[:cursor:-1], name[cursor+1:]+name[:cursor]    각각 왼쪽, 오른쪽 방향인데, 생각해보니까 서로 reversed 관계
        # A가 아닌 놈(=F)이 가까이 있는 것을 찾는 게 아닌,
        load = name[cursor+1:]+name[:cursor]
        l_dist, r_dist = load.index("F")+1, load[::-1].index("F")+1
        answer += min(l_dist, r_dist)
        print(load, l_dist, r_dist)
        cursor = (cursor + (l_dist if l_dist <= r_dist else len(load)-r_dist+1)) % len(name)
        # 왼쪽 오른쪽 모두 같은 거리일 경우에, 오른쪽으로 가야된다는 걸 명시도 안해주고 질문에서 찾았다... https://programmers.co.kr/questions/12677
        # 정말 나빴다...... 이 마지막 테스트 케이스 때문에 1시간 동안 삽질했다......
        name[cursor] = "A"
        print(answer, cursor, name)
    return answer


# 테스트 코드
print(solution("JAN"))
print(solution("JAZ"))
print(solution("JEROEN"))
print(solution("AAPAAAPAA"))
print(solution("APAAAAAJA"))
print(solution("AABAAAAAAAAABBB"))
# testCase for 11
print(solution("BBBAAAB"))      # 8이지만 테스트케이스 통과하려면 9가 나와야함
print(solution("ABABAAAAABA"))  # 11
# testCase 1
print(solution("BAABA"))
print(solution("ABABA"))
print(solution("BABAB"))
print(solution("BBABAAAB"))

