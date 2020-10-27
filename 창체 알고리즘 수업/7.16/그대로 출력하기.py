while True:
    try:
        print(input())
    except:
        break


# 다른 방법
import sys
print(sys.stdin.read())


# 또 다른 방법
print(open(0).read())
