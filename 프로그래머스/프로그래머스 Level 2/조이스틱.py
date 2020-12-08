def solution(name):
    a_cnt_l, a_cnt_r, a_cnt_l_bool, a_cnt_r_bool = 0, 0, True, True
    for i in range(1, len(name)):
        a_cnt_l, a_cnt_l_bool = (a_cnt_l+1, True) if a_cnt_l_bool and name[-i] == "A" else (a_cnt_l, False)
        a_cnt_r, a_cnt_r_bool = (a_cnt_r+1, True) if a_cnt_r_bool and name[i] == "A" else (a_cnt_r, False)
    answer = len(name) - max(a_cnt_l, a_cnt_r) - 1
    for i in name.replace("A", ""):
        print(i, ord(i), ord(i) - 65, 90 - ord(i) + 1)
        answer += min(ord(i) - 65, 90 - ord(i) + 1)
    return answer


# 테스트 코드
print(solution("JAZ"))
print(solution("JEROEN"))
print(solution("JAN"))
print(solution("AAPAAAPAA"))
