def middle_element(lst):
    middle_element = 0
    if len(lst) % 2 == 1:
        middle_element = lst[int(len(lst)/2)]
        return middle_element
    else:
        middle_element = (lst[(int(len(lst)/2) - 1)] +
                          lst[int(len(lst)/2)]) / 2
        return middle_element


print(middle_element([5, 2, -10, -4, 4, 5]))
