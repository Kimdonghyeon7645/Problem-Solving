def solution(park, routes):
    pos = [[i, park[i].find('S')] for i in range(len(park)) if 'S' in park[i]][0]
    for r in routes:
        b,n = r[0],int(r[2:])
        if b == 'N':
            if pos[0]-n >= 0 and not [1 for i in range(n) if park[pos[0]-i-1][pos[1]] == 'X']:
                pos[0]-=n
        elif b == 'S':
            if pos[0]+n < len(park) and not [1 for i in range(n) if park[pos[0]+i+1][pos[1]] == 'X']:
                pos[0]+=n
        elif b == 'W':
            if pos[1]-n >= 0 and not [1 for i in range(n) if park[pos[0]][pos[1]-i-1] == 'X']:
                pos[1]-=n
        elif b == 'E':
            if pos[1]+n < len(park[0]) and not [1 for i in range(n) if park[pos[0]][pos[1]+i+1] == 'X']:
                pos[1]+=n
    return pos