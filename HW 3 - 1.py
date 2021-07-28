def my_func (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "y не может быть нулём"
    except ValueError:
        return "введите число"
print(my_func(int(input("Ввести значение x = ")), int(input("Ввести значение y = "))))
