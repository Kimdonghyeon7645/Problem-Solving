class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return f"현재 스텍의 상태 : {self.stack}"

    def push(self, num):
        self.stack += num

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def __sizeof__(self):
        return len(self.stack)

    def empty(self):
        if self.stack:
            return 1
        else:
            return 0


class MyStack(Stack):
    def run(self):
        pass


st = MyStack()

print(st)
