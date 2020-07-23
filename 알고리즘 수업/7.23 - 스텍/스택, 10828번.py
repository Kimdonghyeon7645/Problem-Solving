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
        print(stk.pop())
    elif cmd.startswith('top'):
        print(stk[-1])
    elif cmd.startswith('size'):
        print(len(stk))
    elif cmd.startswith('empty'):
        print(0 if stk else 1)
