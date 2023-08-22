def solution(cards1, cards2, goal):
    i1 = i2 = 0
    for g in goal:
        if i1 < len(cards1) and cards1[i1] == g:
            i1+=1
        elif i2 < len(cards2) and cards2[i2] == g:
            i2+=1
        else:
            return "No"
    return "Yes"