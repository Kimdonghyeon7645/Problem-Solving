import queue, sys

q = queue.Queue()
for _ in range(int(input())):
    cmd = sys.stdin.readline().rstrip()
    if cmd == 'pop':
        print(q.get() if not q.empty() else -1)
    elif cmd == 'size':
        print(q.qsize())
    elif cmd == 'empty':
        print(q.empty())
    elif cmd == 'front':
        print(list(q))
