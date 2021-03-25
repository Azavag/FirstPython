import math
import random
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def power(x,y):
    return math.pow(x,y)
def modulus(x):
    return math.fabs(x)
def fact(x):
    return math.factorial(x)
def arccos(x):
    return math.acos(x)
def rand_num():
    return random.random

while True:
    print("Ноль в качестве знака операции"
          "\nзавершит работу программы")
    sign = input("Знак (+,-,*,/, ^(для степени),"
                 "\nabs(для модуля), !(для факториала), arccos(для аркосинуса)(-1 до 1)," 
                 "\nrand(для вывода случайного числа): ")
    if sign == '0':
        break
    if sign in ('+', '-', '*', '/', '^'):
        x = float(input("x="))
        y = float(input("y="))
        if sign == '+':
            print(add(x,y))
        elif sign == '-':
            print(subtract(x,y))
        elif sign == '*':
            print(multiply(x,y))
        elif sign == '/':
            if y != 0:
                print(divide(x,y))
            else:
                print("Деление на ноль!")
        elif sign == '^':
            print(power(x,y))
    elif sign in ("abs", "!", "arccos"):
        x = float(input("x="))
        if sign == "abs":
            print(modulus(x))
        elif sign == '!':
            print(fact(x))
        elif sign == "arccos":
            if x > 1 or x <-1:
                print("Число должно быть в диапозоне [-1; 1]")
                continue;
            else:
                print(arccos(x))          
    elif sign == "rand":
        print(rand_num)            
    else:
        print("Неверный знак операции!")
    print("\n")
