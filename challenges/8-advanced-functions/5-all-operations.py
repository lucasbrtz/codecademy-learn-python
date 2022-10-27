def lots_of_math(a, b, c, d):
    print(a + b)
    print(c - d)
    print((a + b) * (c - d))
    return ((a + b) * (c - d)) % a


print(lots_of_math(1, 2, 3, 4))
print(lots_of_math(1, 1, 1, 1))
