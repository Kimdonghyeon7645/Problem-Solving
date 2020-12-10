def solution(n):
    index_li = [list(map(str, range(len(n))))]
    for i in range(len(n)-1):
        index_li.append([])
        for index in index_li[i]:
            index_li[i+1].extend([index+str(ele) for ele in range(len(n)) if str(ele) not in index])
    word_set = set(int(''.join(n[int(j)] for j in i)) for li in index_li for i in li)
    word_set -= {0, 1}
    answer = len(word_set)
    for word in word_set:
        for i in range(2, int(word ** 1/2)+1):
            if word % i == 0:
                answer -= 1
                break
    return answer


# 테스트 코드
print(solution("71"))
print(solution("101"))
# print(solution("000001"))
print(solution("9999999"))
