def divisible_by_ten(num):
    remainder = num % 10
    if remainder == 0:
        return True
    else:
        return False


print(divisible_by_ten(20))
print(divisible_by_ten(25))
