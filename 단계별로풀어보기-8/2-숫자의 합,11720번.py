input()
# print(sum(map(int, list(input())))) # 와 같이 해도 되지만,
# 근데 input()으로 받는 자료형이 str이라, 이미 시퀀스 자료형이므로 list()로 형변환 할 필요 없음
print(sum(map(int, list(input()))))
