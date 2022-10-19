def append_sum(lst):
    for i in range(3):
        last_numbers = lst[-1] + lst[-2]
        lst.append(last_numbers)
    return lst


print(append_sum([1, 1, 2]))
