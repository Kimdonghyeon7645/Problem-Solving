stk = []
for i in input():
    if i == '(':
        stk += i
    elif stk:
        stk.pop()
    else:
        stk += [-1]
        break
print('YES' if not stk else 'NO')
