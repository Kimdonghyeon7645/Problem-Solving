for i in range(int(input())):
    li = list(map(int, input().split()))[1:]
    ft = round(sum([1 for d in li if d > sum(li) / len(li)]) / len(li) * 100, 3)
    print(f'{ft:0<{6 if ft > 10 else 5}}%')
