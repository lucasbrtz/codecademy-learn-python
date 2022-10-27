def every_three_nums(start):
    lst = []
    if start <= 100:
        while start <= 100:
            lst.append(start)
            start += 3
    return lst

#    a better way to write this code in one line:
#    return list(range(start, 101, 3))


print(every_three_nums(91))
