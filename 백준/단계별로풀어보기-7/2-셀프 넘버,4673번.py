def self_num(i):
    return i + sum([int(j) for j in str(i)])


s = set()
for i in range(1, 10001):
    s.add(self_num(i))
for i in sorted(set(i for i in range(1, 10001)) - s):
    print(i)
