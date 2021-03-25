d_keys = set(input("Введите слова Через запятую\n").split(','))
print(len(d_keys), " -количество слов в списке.\n")
d_values = set(input("Введите список слов с таким же количеством:\n").split(','))
dictionary = dict(zip(d_keys, d_values))

print(dictionary)
