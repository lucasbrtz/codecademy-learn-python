def more_frequent_item(lst, item1, item2):
    item1_count = 0
    item2_count = 0

    for item in lst:
        if item == item1:
            item1_count += 1
        elif item == item2:
            item2_count += 1

    if item1_count < item2_count:
        return item2
    else:
        return item1


print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
