import itertools

# def suma (*var):
#     s = 0
#     for i in var:
#         s += i
#     return s
#
# print(suma(1,2,3))


# a = [1, 2, 3]
# print(id(a))
#
# a.append(10)
# a.pop(1)
# print(id(a))
#
#
# print(a)

# maxim = "Поехал на дачу"
# print(maxim)
# print(maxim.split("а"))

# a = "1121212121111122222222222112111111111111111111222222222222222211121212121211112222221112112111"
# print(a)
# a = a.split("2")
# print(a)
# max_1 = len(a[0])
# for i in a:
#     if len(i) > max_1:
#         max_1 = len(i)
# print(max_1)


# a = "1121212121111122222222222112111111111111111111222222222222222211121212121211112222221112112111"
# b = a.replace("2","A",1)
# print(b)

# a = [1, 2, 3, 4, 5]
# # b = itertools.permutations(a)
# # print(list(b))
# # print(len(list(b)))
# c = itertools.product(a,repeat=4)
# print(list(c))
#
# print("1" in "123454")

# a = '8' * 70
#
# while '2222' in a or '8888' in a:
#     if '2222' in a:
#         a = a.replace('2222','88', 1)
#     else:
#         a = a.replace('8888', '22', 1)
# print(a)


# a = 3 * 4 ** 38 + 2 * 4 ** 23 + 4 ** 20 + 3 * 4 ** 5 + 2 * 4 ** 4 + 1
# print(a)
# b = len(str(a))
# print(b)
# print(hex(a))


def f(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return f(a+1, b) + f(a*2 , b)

print(f(1,20))