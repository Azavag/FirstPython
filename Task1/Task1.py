number = input("Введите первое число ")
border_number = input("Введите второе число ")
if number > 3*border_number:
    print("первое число больше пограничного в 3 раза")
elif number < border_number:
    print("Первое число меньше второго")
elif number > border_number:
    print("Первое число больше второго")

