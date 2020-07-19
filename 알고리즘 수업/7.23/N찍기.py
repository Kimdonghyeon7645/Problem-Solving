for i in range(int(input())): print(str(i+1))
# 이거말고 아래처럼도 할 수 있다.
print(*[i for i in range(1, int(input())+1)], sep='\n')
# 이 코드를 줄이면 이 것도 가능하다.
print(*range(1, int(input())+1), sep='\n')
