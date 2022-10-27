def larger_sum(lst1, lst2):
    lst1_sum = 0
    lst2_sum = 0

    for item in lst1:
        lst1_sum += item
    for item in lst2:
        lst2_sum += item

    if lst1_sum < lst2_sum:
        return lst2
    else:
        return lst1


print(larger_sum([1, 9, 5], [2, 3, 7]))
