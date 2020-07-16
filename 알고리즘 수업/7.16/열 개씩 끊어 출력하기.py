li = input()
print(*[li[i:i+10] if len(li)-i > 10 else li[i:len(li)] for i in range(0, len(li)+1, 10)], sep='\n')
