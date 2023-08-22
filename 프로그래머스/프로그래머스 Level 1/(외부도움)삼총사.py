"""
제약조건이 3<=len(number)<=13 이므로
무식하게 BP 방식(삼중 for문)으로 해결 가능
"""
def solution(number):
    answer = 0
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            for k in range(j+1, len(number)):
                if number[i]+number[j]+number[k] == 0:
                    answer += 1
    return answer