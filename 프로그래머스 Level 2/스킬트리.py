def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        # print(tree)
        idx = 0
        for ch in tree:
            # print(ch, idx, skill[idx], skill[idx+1:])
            if ch in skill[idx+1:]:
                # print('불가능')
                break
            elif ch is skill[idx]:
                # print('맞워요')
                idx += 1
            if idx >= len(skill) or ch == tree[-1]:
                answer += 1
                # print('가능')
                break
    return answer


# 아래는 테스트 코드
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))