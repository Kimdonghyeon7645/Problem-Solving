def solution(k, m, score):
    s = sorted(score,reverse=True)
    return sum(s[m*i+m-1]*m for i in range(len(score)//m))
    # [s[m*i:m*i+m] for i in range(len(score)//m)]