def solution(food):
    f = ''.join(str(i)*(n//2) for i,n in enumerate(food))
    return f+'0'+f[::-1]