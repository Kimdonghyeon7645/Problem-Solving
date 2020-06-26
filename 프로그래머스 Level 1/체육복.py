def solution(n, lost, reserve):
    lost_ = lost.copy()
    for pp in lost_:
        if pp in reserve:
            lost.remove(pp)
            reserve.remove(pp)
    lost_ = lost.copy()
    for people in lost_:
        for mazin in reserve:
            if mazin+1 == people or mazin-1 == people:
                lost.remove(people)
                reserve.remove(mazin)
                break
    return n - len(lost)
