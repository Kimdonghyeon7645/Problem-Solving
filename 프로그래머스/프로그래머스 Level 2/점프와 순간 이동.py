def solution(n):
    ans,i = n,0
    while ans > 1:
        if ans%2:
            ans-=1
            i+=1
        else:
            ans//=2
    return i+1