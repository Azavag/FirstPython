title_of_veg = []
amounts_of_veg = []
for count in range(0, 3):
    word = input("Введите название овощей ")
    title_of_veg.append(word)

for str in title_of_veg:
    print(str.lower())
for str in title_of_veg:
    print(str.upper())
for str in title_of_veg:
    print(str.title())

for count in range(0, len(title_of_veg)):
    amount = int(input("Введите количество овощей "))
    amounts_of_veg.append(amount)
for count in range(0, len(title_of_veg)):
    print("В ящике лежит {amount} {title}. ".format(title=title_of_veg[count], amount = amounts_of_veg[count]))
    