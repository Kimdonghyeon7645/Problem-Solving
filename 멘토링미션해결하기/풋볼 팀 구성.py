positions = {'Wide Receiver': [4.5, 150, 200],
            'Lineman': [6.0, 300, 500],
            'Quarterback': [5.0, 200, 300]}

answer = ''
speed, weight, power = map(lambda x: float(x) if '.' in x else int(x), input().split())
for posit, info in positions.items():
    if speed <= info[0] and weight >= info[1] and power >= info[2]:
        answer += posit+' '
print(answer if answer else 'No positions')
