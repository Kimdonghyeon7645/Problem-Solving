def solution(strings, n):
    li = [[] for i in range(ord('a'), ord('z')+1)]
    for yo in strings:
        li[ord(yo[n]) - 97].append(yo)
    print(li)


solution(['sun', 'bed', 'car'], 1)
solution(['abce', 'abcd', 'cdx'], 2)
