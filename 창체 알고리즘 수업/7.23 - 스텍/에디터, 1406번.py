import sys

left, right = list(input()), []
for _ in range(int(input())):
    cmd = sys.stdin.readline().rstrip()
    if cmd == 'L' and left:
        right.append(left.pop())
    elif cmd == 'D' and right:
        left.append(right.pop())
    elif cmd == 'B' and left:
        left.pop()
    elif cmd.startswith('P'):
        left.append(cmd.split()[-1])
print(''.join(left + list(reversed(right))))

# sys.stdin.readline().rstrip() 를 input() 대신에 사용하면 속도가 엄청 빠르다!
# 특히 입력(input())을 N번 반복하면 될 수록 그 속도 차이가 커진다!
