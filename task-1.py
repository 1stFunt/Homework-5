# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
def degree(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * degree(a, b - 1))


a = int(input("Число: "))
b = int(input("Степень: "))
print(degree(a, b))