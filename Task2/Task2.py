counter = 0
string = input("Введите строку ")
print("Длина строки = ", len(string))

for letter in string:
    counter += 1
    if (counter == 3 or letter == string[-1]):
        continue
    if letter == 'c':
        print("В строке пристутсвует буква 'C' ")
    print(letter)

