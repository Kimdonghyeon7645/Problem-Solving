m = int(input())
for i in range(1, 10):
    print(m, '*', i, '=', m*i)
# 근데 이거 말고도 이것도 된다.
m = int(input())
print(*[f"{m} * {i} = {m * i}" for i in range(1, 10)], sep='\n')
