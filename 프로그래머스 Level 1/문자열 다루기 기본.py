def solution(s):
    return len(s) in [4, 6] and s.isdigit()


print(solution('a234'))
print(solution('1234'))
