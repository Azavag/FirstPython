import os.path
def put_words():
    return set(input("Введите слова через запятую\n").split(','))
def list_lenght(set):
    return len(set)
def create_dict(keys, values):
    return dict(zip(keys, values))
d_keys = put_words()
print(list_lenght(d_keys))
d_values = put_words()
dictionary = create_dict(d_keys, d_values)

filename = input("Введите название файла: ")

if(os.path.exists(filename)):
    f = open(filename, "r+")
    text = f.read()
    f.seek(0)
    f.truncate()
else:
    f = open(filename, "w+")
    text = ''
for key,val in dictionary.items():
    f.write('{}:{}\n'.format(key,val))
if(text != ''):
    f.write(text)
f.close()
