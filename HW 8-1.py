class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        date = []

        for i in day_month_year.split():
            if i != '-': date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f"Все верно"
                else:
                    return f'Некорректный год'
            else:
                return f'Некорректный месяц'
        else:
            return f'Некорректный день'

    def __str__(self):
        return f'Текущая дата {Date.extract(self.day_month_year)}'


today = Date('12 - 8 - 2021')
print(today)
print(Date.valid(11, 1, 2021))
print(today.valid(11, 13, 2001))
print(Date.extract('11 - 11 - 2011'))
print(today.extract('11 - 8 - 2021'))
print(Date.valid(1, 11, 2000))
