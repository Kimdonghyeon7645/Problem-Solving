def solution(record):
    user_db = dict()
    answer = []
    for cmd in record:
        cmd = cmd.split()
        if cmd[0] in ["Enter", "Change"]:
            user_db.update({cmd[1]: cmd[2]})
            if cmd[0] == "Enter":
                answer.append(f"{cmd[1]}/님이 들어왔습니다.")
        else:
            answer.append(f"{cmd[1]}/님이 나갔습니다.")
    return [user_db[text.split('/')[0]]+text.split('/')[-1] for text in answer]


# 테스트 코드
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
