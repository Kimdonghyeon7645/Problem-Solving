def sequential_search(n: int, li: list, num: int) -> int:
    for i in range(n):
        if li[i] == num:
            return i
        elif i == n-1:
            return -1


print(sequential_search(5, [1, 4, 3, 2, 5], 3))


# 내장함수를 써보면?
def sequential_search(n, li, num): return li.index(num)


print(sequential_search(5, [1, 4, 3, 2, 5], 3))
