"""
따로 배열을 할당하지 않고 인덱스로만 풀이법
"""
def solution(ingredient):
    r=i=0
    while i < len(ingredient)-3:
        while ingredient[i:i+4] == [1,2,3,1]:
            for _ in range(4): ingredient.pop(i)
            i=i-3 if i > 2 else 0
            r+=1
        i+=1
    return r


"""
s=s[:4] 보다 s.pop()을 4번 반복하는게 낫다.
무려 93배까지 속도차이가 난다...

이 사실을 몰라서(ㅠㅠ) 시간초과 때문에 위 함수로 우회해서 풀었으나,
성능상 아래가 더 효율적이니 아래 함수 방식을 추천
"""
def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for _ in range(4): s.pop()
            # s=s[:-4]
    return cnt