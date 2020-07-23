class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return f"현재 스텍의 상태 : {self.stack}"

    def my_push(self, num):
        self.stack += num

    def my_pop(self):
        return self.stack.pop()

    def my_top(self):
        return self.stack[-1]

    def my_size(self):
        return len(self.stack)

    def my_empty(self):
        if self.stack:
            return 1
        else:
            return 0


class MyStack(Stack):
    def run(self, cmd):
        if cmd.startswith('push'):
            return self.stack.my_push(cmd.split()[-1])
        else:
            func = 'my_' + cmd
            return self.stack.func()


st = MyStack()
cmds = ''
# cmds = open(0).read()
while True:
    temp = input()
    if temp:
        cmds += temp+'\n'
    else:
        break
for cmd in cmds.split():
    print(st.run(cmd))
print(st)
