def max_num(nums):
    maximum = nums[0]
    for number in nums:
        if maximum < number:
            maximum = number
    return maximum


print(max_num([50, -10, 0, 75, 20]))
