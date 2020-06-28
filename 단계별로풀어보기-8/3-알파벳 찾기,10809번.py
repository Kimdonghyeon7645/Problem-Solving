w = input()
for i in range(97, 123):
    print(w.find(chr(i)), end=' ')

# 아래와 같이 해도 가능
w = input()
print(*[w.find(chr(i))for i in range(97, 123)], end=' ')

# 숏코딩 모범답안, 이건 인정
print(*map(input().find, map(chr, range(97, 123))))
