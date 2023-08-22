def solution(n, m, section):
    i = c = 0
    for s in section:
        if s > i:
            i = s+m-1
            c += 1
    return c