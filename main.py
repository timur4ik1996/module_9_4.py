from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = map(lambda x, y: x == y, first, second)
print(list(result))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'w', encoding='utf- 8')
        for i in data_set:
            file.write(str(i) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = list(words)

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
