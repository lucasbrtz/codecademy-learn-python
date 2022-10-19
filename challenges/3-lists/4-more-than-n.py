def more_than_n(lst, item, n):
    index = 0
    for element in lst:
        if element == item:
            index += 1
    if index > n:
        return True
    else:
        return False


print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
