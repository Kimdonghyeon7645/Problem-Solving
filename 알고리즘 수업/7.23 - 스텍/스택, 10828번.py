stk = []
# cmds = open(0).read()
cmds = ''
while True:
    cmd = input()
    if cmd:
        cmds += cmd + '/n'
    else:
        break
for cmd in cmds.split('/n'):
    if cmd.startswith('push'):
        stk.append(cmd.split()[1])
    elif cmd.startswith('pop'):
        if cmd:
            print(stk.pop())
        else:
            print(-1)
    elif cmd.startswith('top'):
        if cmd:
            print(stk[-1])
        else:
            print(-1)
    elif cmd.startswith('size'):
        print(len(stk))
    elif cmd.startswith('empty'):
        print(0 if stk else 1)
