w = input()
s = 0
for i in ['dz=', 'lj', 'nj', 'c=', 'c-', 'd-', 's=', 'z=']:
    s += w.count(i)
#    print(i, w.count(i), s, w)
    w = w.replace(i, '0')
print(s + len(w.replace('0', '')))
