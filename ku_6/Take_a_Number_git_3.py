# Число 89— это первое целое число, состоящее более чем из одной цифры, которое удовлетворяет свойству, частично представленному в названии этого ката. Что толку говорить "Эврика"? Потому что эта сумма дает одно и то же число.

# В результате:89 = 8^1 + 9^2
#
# Следующим числом обладающего этим свойством является 135.
#
# Посмотрите это свойство еще раз:135 = 1^1 + 3^2 + 5^3
#
# Нам нужна функция для сбора этих чисел, которая может принимать два целых числа a,
# bкоторая определяет диапазон [a, b](включительно) и выводит список отсортированных
# чисел в диапазоне, удовлетворяющем описанному выше свойству.
#
# Давайте рассмотрим некоторые случаи:
#
# sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
# Если в диапазоне [a, b] таких чисел нет, функция должна вывести пустой список.
#
# sum_dig_pow(90, 100) == []


def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    dig_pow = []
    for i in range(a, b+1):
        i = str(i)
        s = 1 # степень последовательности
        z = 0 # сумма квадратов
        for j in i: # разбиваю число на слагаемые
            z += int(j) ** s
            s += 1 # увеличиваю степень
        if int(i) == z:
            dig_pow.append(int(i))

    return dig_pow

print(sum_dig_pow(1, 10))
print(sum_dig_pow(1, 100))
print(sum_dig_pow(10, 89))
print(sum_dig_pow(10, 100))
print(sum_dig_pow(90, 100))
print(sum_dig_pow(89, 135))



# def it1():
#     test.assert_equals(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
#     test.assert_equals(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
#     test.assert_equals(sum_dig_pow(10, 89), [89])
#     test.assert_equals(sum_dig_pow(10, 100), [89])
#     test.assert_equals(sum_dig_pow(90, 100), [])
#     test.assert_equals(sum_dig_pow(89, 135), [89, 135])
#     
#
#
# def dig_pow(n):
#     return sum(int(x)**y for y,x in enumerate(str(n), 1))
#
# def sum_dig_pow(a, b):
#     return [x for x in range(a,b + 1) if x == dig_pow(x)]