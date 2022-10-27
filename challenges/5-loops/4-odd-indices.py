def odd_indices(lst):
    new_list = []
    for index in range(len(lst)):
        if index % 2 == 1:
            new_list.append(lst[index])
    return new_list


print(odd_indices([4, 3, 7, 10, 11, -2]))
