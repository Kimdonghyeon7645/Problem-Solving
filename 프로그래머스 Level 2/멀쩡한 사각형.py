#  55.6 / 100.0 점
def solution(w, h):
    enable = 0
    for i in range(1, h+1):
        enable += (int(w/h * i)-1 if w/h * i == int(w/h * i) and i > 0 else int(w/h * i)) - int(w/h * (i-1)) + 1
    return (w * h) - enable


print(solution(8, 12))
