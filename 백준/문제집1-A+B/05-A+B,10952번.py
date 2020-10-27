while True:
    a = input()
    if a == '0 0':
        break
    print(eval('+'.join(a.split())))
