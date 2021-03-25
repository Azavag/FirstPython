def put_words():
    return set(input("Введите слова Через запятую\n").split(','))
def list_lenght(set):
    return len(set)
def create_dict(keys, values):
    return dict(zip(keys, values))
d_keys = put_words()
print(list_lenght(d_keys))
d_values = put_words()
dictionary = create_dict(d_keys, d_values)

print(dictionary)

