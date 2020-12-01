# def solution(s):              # 숫자를 한 글자씩 가져옴 -> 두자리 이상의 숫자도 한자리 숫자로 인식하는 문제 발생
#     li = [int(i) for i in s if i.isdigit()]
#     return list(sorted(set(li), key=lambda x: -li.count(x)))

def solution(s):
    li = [int(i) for i in s.replace("{", "").replace("}", "").split(",")]
    return list(sorted(set(li), key=lambda x: -li.count(x)))


# 테스트 코드
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{20,111},{111}}"))
