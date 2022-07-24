# a = 98687657858657645646755645641654562468975956784769680696765478
# c = 246
# z = 0
# b = 1
#
# while c >= b:
#     if c % b == 0:
#         print(b)
#         z += b ** 2
#     b += 1
# print(z)


def list_squared (m, n):
    c = m
    list_sq = []
    while m <= n:
        b = 1
        z = 0
        while c >= b:
            list_c_z = []
            if c % b == 0:
                z += b ** 2
            b += 1
        if z ** 0.5 == int(z ** 0.5):
            list_c_z.append(c)
            list_c_z.append(z)
            list_sq.append(list_c_z)
        c += 1
        m += 1

    return list_sq


print(list_squared(1, 250))
print(list_squared(42, 250))\
print(list_squared(250, 500))