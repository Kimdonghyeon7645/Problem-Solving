stk = []
cmds = []
for i in range(int(input())):
    cmds.append(input())
for cmd in cmds:
    if cmd.startswith('push'):
        stk.append(cmd.split()[1])
    elif cmd.startswith('pop'):
        print(stk.pop() if stk else -1)
    elif cmd.startswith('top'):
        print(stk[-1] if stk else -1)
    elif cmd.startswith('size'):
        print(len(stk))
    elif cmd.startswith('empty'):
        print(0 if stk else 1)
