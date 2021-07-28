def div(*args):

    try:
        arg1 = int(input("Введите значение "))
        arg2 = int(input("Введите значение "))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка'
    except ZeroDivisionError:
        return "Некорректное значение! Нельзя использовать ноль при делении!"

    return res
print(f'Результат  {div()}')
