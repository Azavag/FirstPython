import math
import random
class Calc:
    def operations(self, sign):
        if sign in ('+', '-', '*', '/', '^'):
            x = float(input("x="))
            y = float(input("y="))           
            if sign == '+':
                return print(x + y)
            elif sign == '-':
                 return print(x - y)
            elif sign == '*':
                return print(x * y)
            elif sign == '/':
                if y == 0:
                    return print("Деление на 0.")
                else:
                    return print(x / y)
            elif sign == '^':
                 return print(math.pow(x, y))
        elif sign in ("abs", "!", "arccos"):
            x = float(input("x="))
            if sign == "abs":
                return print(math.fabs(x))
            elif sign == '!':
                return print(math.factorial(x))
            elif sign == "arccos":                 
                return print(math.acos(x))          
        elif sign == "rand":
            return print(random.random())            
        else:
            print("Неверный знак операции!")
        print("\n")

while True:
    print("Ноль в качестве знака операции"
          "\nзавершит работу программы\n")
    sign = input("Знак (+,-,*,/, ^(для степени),"
                 "\nabs(для модуля), !(для факториала), arccos(для аркосинуса)(-1 до 1)," 
                 "\nrand(для вывода случайного числа)."
                 "\nВведите знак нужной операции: ")   
    if sign == '0':
        break
    calc = Calc()
    calc.operations(sign)
   
