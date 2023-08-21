def solution(a, b, n):
    c = 0
    while n >= a:
        c+=n//a*b
        n=n//a*b+n%a 
    return c