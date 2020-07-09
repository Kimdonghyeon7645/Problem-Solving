def binary_search(n, li, num):
    low = 0
    middle = n // 2
    hight = n - 1
    while True:
        if num == li[middle]:
            return middle
        elif li[hight] >= num > li[middle]:
            low = middle + 1
            middle = (middle + hight) // 2
        elif li[low] <= num < li[middle]:
            hight = middle - 1
            middle = (middle + low) // 2
        else:
            return -1


li2 = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(binary_search(len(li2), li2, 33))
