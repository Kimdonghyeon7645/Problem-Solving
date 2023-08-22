def solution(keymap, targets):
    keys = {}
    res = []
    for k in keymap:
        for i in range(len(k)):
            keys[k[i]] = min(keys[k[i]],i+1) if k[i] in keys else (i+1)
    for t in targets:
        r = 0
        for c in t:
            if c in keys:
                r += keys[c]
            else:
                r = -1
                break
        res.append(r)
    return res