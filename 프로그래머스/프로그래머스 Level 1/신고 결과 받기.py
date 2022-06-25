def solution(id_list, report, k):
    users = dict([(i, [0, [], 0]) for i in id_list])
    # for rep in report:
    #   if users[rep.split()[1]][1] in rep.split()[0]:
    for rep in set(report):
        users[rep.split()[1]][0] += 1
        users[rep.split()[1]][1].append(rep.split()[0])
    for user in users.values():
        if user[0] >= k:
            for user_id in user[1]:
                users[user_id][2] += 1
    return [user[2] for user in users.values()]


if __name__ == '__main__':
    print(solution(["muzi", "frodo", "apeach", "neo"],
             ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
    print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
