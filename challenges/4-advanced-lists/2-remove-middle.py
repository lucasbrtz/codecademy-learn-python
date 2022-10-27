def remove_middle(lst, start, end):
    for i in range(end):
        lst.remove(lst[start])
    return lst


print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
