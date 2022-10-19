def combine_sort(lst1, lst2):
    lst = lst1 + lst2
    lst.sort()
    return lst


print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
