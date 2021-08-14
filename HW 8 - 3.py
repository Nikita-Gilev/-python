class NotANumberException(Exception):
    def __init__(self, *args):
        self.result_list = []
while True:
    value = input('Введите числовой элемент для добавления в список или "stop" для выхода: ')

    if value == 'stop':
        print(f'Список на момент выхода{result_list}')
        break

    try:
        if not value.isnumeric():
            raise NotANumberException('NaN!')
        result_list.append(int(value))
    except NotANumberException as error:
        print('Вы ввели не число')
