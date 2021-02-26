import math
import random
print("Ноль в качестве знака операции"
      "\nзавершит работу программы")
while True:
    sign = input("Знак (+,-,*,/, ^(для степени),"
    "\nabs(для модуля), !(для факториала), arccos(для аркосинуса)(-1 до 1), \nrand(для вывода случайного числа): ")
    if sign == '0':
        break
    if sign in ('+', '-', '*', '/', '^'):
        x = float(input("x="))
        y = float(input("y="))
        if sign == '+':
            print("%.2f" % (x+y))
        elif sign == '-':
            print("%.2f" % (x-y))
        elif sign == '*':
            print("%.2f" % (x*y))
        elif sign == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
        elif sign == '^':
            print(math.pow(x,y))

    elif sign in ("abs", "!", "arccos"):
        x = float(input("x="))
        if sign == "abs":
            print(abs(x))
        elif sign == '!':
            print(math.factorial(x))
        elif sign == "arccos":
            if x > 1 or x <-1:
                print("Число должно быть в диапозоне [-1; 1]")
                continue;
            else:
                print(math.acos(x))          
    elif sign == "rand":
        print(random.uniform(0, 100))            
    else:
        print("Неверный знак операции!")
    print("\n")