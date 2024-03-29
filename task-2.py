# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
def sum(a, b):
    a += 1
    b -= 1
    if b > 0:
        return sum(a, b)
    return a


a = int(input())
b = int(input())
print(sum(a, b))