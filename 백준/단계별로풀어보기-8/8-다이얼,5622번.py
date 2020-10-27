word = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
print(sum(dial.index(j) + 3 for j in dial for i in word if i in j))
