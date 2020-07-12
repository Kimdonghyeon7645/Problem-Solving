def solution(phone_number):
    return '*'*(len(phone_number)-4) + phone_number[-4:]


# 아래는 테스트 코드
print(solution('01012345678'))
print(solution('0277887788'))
