"""
.index() 안쓰고 오로지 인덱스와 dict(해시테이블)로만 사용하여 구현하면 된다.
"""
def solution(players, callings):
    pr = dict(list((players[i], i+1) for i in range(len(players))))
    rp = dict(list((i+1, players[i]) for i in range(len(players))))
    for p in callings:
        r = pr[p]
        nr = r-1
        np = rp[nr]
        rp[nr] = p
        rp[r] = np
        pr[np] = r
        pr[p] = nr
    return [p for p in rp.values()]


def solution(players, callings):
    pla_dic = {key: i for i, key in enumerate(players)}

    for p in callings:
        c = pla_dic[p]
        pla_dic[p] -= 1
        pla_dic[players[c-1]] += 1
        players[c-1], players[c] = players[c], players[c-1]

    return players