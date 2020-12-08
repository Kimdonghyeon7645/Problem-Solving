def solution(n):
    maximum = int(''.join(sorted(n, reverse=True)))
    so_su = list(range(2, maximum+1))
    i = 0
    while i < len(so_su):
        so_su = so_su[:i+1] + [e for e in so_su[i+1:] if e % so_su[i] != 0]
        i += 1
        print(so_su)
    return


# 테스트 코드
print(solution("100"))
