import math
import random
class Calc:
    def put_numbers(self, num1, num2 = 0):
        self.x = num1
        self.y = num2

    def operations(self, sign):
        if sign in ('+', '-', '*', '/', '^'):           
            if sign == '+':
                return print(self.x + self.y)
            elif sign == '-':
                 return print(self.x - self.y)
            elif sign == '*':
                return print(self.x * self.y)
            elif sign == '/':
                if self.y == 0:
                    return print("Деление на 0.")
                else:
                    return print(self.x / self.y)
            elif sign == '^':
                 return print(math.pow(self.x, self.y))

        elif sign in ("abs", "!", "arccos"):
            if sign == "abs":
                return print(math.fabs(self.x))
            elif sign == '!':
                return print(math.factorial(self.x))
            elif sign == "arccos":     
                if self.x >= -1 and self.x <= 1:
                    return print(math.acos(self.x))     
                else:
                    return print("Число должно находится в диапозоне от -1 до 1")
        elif sign == "rand":
            return print(random.random())    
        else: 
            return print("Неправильный знак!\n")

while True:
    print("\nНоль в качестве знака операции"
          "\nзавершит работу программы\n")
    sign = input("Знак (+,-,*,/, ^(для степени),"
                 "\nabs(для модуля), !(для факториала), arccos(для аркосинуса)(-1 до 1)," 
                 "\nrand(для вывода случайного числа)."
                 "\nВведите знак нужной операции: ")   
    if sign == '0':
        break
    calc = Calc()
    if sign in ('+', '-', '*', '/', '^'): 
        calc.put_numbers(float(input("x=")), float(input("y=")))
    elif sign in ("abs", "!", "arccos"):
        calc.put_numbers(float(input("x=")))

    calc.operations(sign)
   

