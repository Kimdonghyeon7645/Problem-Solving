def solution(s):
    x = ""
    answer=xcnt=nxcnt=0
    for c in s:
        if not xcnt:
            x=c
        if x==c:
            xcnt+=1
        else:
            nxcnt+=1
        if xcnt==nxcnt:
            answer+=1
            xcnt=nxcnt=0
    if xcnt or nxcnt:
        answer+=1
    return answer