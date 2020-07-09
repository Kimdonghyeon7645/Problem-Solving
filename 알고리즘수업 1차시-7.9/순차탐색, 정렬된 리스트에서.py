def sequential_search(n: int, li: list, num: int) -> int:
    for i in range(n):
        if li[i] == num:
            return i
        elif num > li[i]:
            return -1


print(sequential_search(5, [1, 2, 3, 4, 5], 3))
print(sequential_search(5, [1, 2, 3, 4, 5], 6))


# 내장함수를 써보면?
def sequential_search(n, li, num):
    return str(li).find(num)


print(sequential_search(5, [1, 2, 3, 4, 5], 3))
print(sequential_search(5, [1, 2, 3, 4, 5], 6))
