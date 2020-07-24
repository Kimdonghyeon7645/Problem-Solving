stk = []
cmds = []
for i in range(int(input())):
    cmds.append(input())
for cmd in cmds:
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
