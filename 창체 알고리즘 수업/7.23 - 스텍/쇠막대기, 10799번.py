arrangement = input()
answer = bar = 0
for i in range(len(arrangement)):
    if arrangement[i] == '(':
        if arrangement[i+1] == '(':
            bar += 1
        else:
            answer += bar
    elif arrangement[i-1] == ')':
        bar -= 1
        answer += 1
print(answer)
