def solution(name, yearning, photo):
    dic = dict(zip(name, yearning))
    return [sum(dic[n] if n in dic else 0 for n in p) for p in photo]