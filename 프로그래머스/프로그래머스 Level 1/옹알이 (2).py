def solution(babbling):
    for i in range(len(babbling)):
        for w in ["aya", "ye", "woo", "ma"]:
            babbling[i] = babbling[i].replace(w*2,'=').replace(w,'-')
    return sum(1 for b in babbling if not b.replace('-',''))