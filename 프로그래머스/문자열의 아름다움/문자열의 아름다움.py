def solution(s):
    answer = 0
    index_li = [(start, end) for start in range(len(s)) for end in range(start, len(s))]
    print(index_li)
    for indexs in index_li:
        start, end = indexs
        left_diff = right_diff = 0
        for i in range(end-start):
            print(start+i, end)
            print(start, end+i)
    return answer


solution("baby")
