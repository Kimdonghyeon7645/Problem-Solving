def solution(s, skip, index):
    r = ""
    for c in s:
        i = j = 0
        while i < index:
            j += 1
            if chr(97+((ord(c)+j-97)%26)) not in skip:
                i += 1
        r += chr(97+((ord(c)+j-97)%26))
    return r