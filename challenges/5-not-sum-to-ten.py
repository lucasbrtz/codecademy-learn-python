def not_sum_to_ten(num1, num2):
    if num1 + num2 == 10:
        return False
    else:
        return True


print(not_sum_to_ten(9, -1))
print(not_sum_to_ten(9, 1))
print(not_sum_to_ten(5, 5))
