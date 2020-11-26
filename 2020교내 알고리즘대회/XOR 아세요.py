a, b, c, d = map(int, input().split())
a_b, b_b = f"{a:0>20b}", f"{b:0>20b}"

x_result = ""
for i in range(20):
    t = a_b[i]
    if b_b[i] == '1':
        t = '0' if a_b[i] == '1' else '1'
    x_result += t
x_result = int('0b'+x_result, 2)

y_result = d
for i in range(c, d):
    y_result = i ^ y_result

print(x_result ^ y_result)
