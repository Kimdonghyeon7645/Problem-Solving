def solution(number, limit, power):
    answer = 1
    for i in range(2,number+1):
        t = 2
        for j in range(2,int(i**(1/2))+1):
            if i % j == 0:
                t += 1 if j == i**(1/2) else 2
        answer += power if t > limit else t
    return answer