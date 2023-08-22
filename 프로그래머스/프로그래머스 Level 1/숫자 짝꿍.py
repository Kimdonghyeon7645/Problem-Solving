def solution(X, Y):
    r = "".join(i*min(X.count(i),Y.count(i)) for i in sorted(set(X) & set(Y))[::-1])
    return ("0" if r[0] == r[-1] == "0" else r) if r else "-1"