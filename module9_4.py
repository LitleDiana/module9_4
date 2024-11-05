first = 'Мама мыла раму'
second = 'Рамена мало было'
result = map(lambda x, y: x == y, first, second)
print(list(result))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for item in data_set:
                file.write(f'{item}/n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])