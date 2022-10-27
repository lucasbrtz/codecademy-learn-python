def double_index(lst, index):
    if len(lst) <= index:
        return lst
    else:
        new_lst = lst[:index]
        new_lst.append(lst[index]*2)
        new_lst += lst[index+1:]
        return new_lst


print(double_index([3, 8, -10, 12], 2))
