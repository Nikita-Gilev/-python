class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} движется'

    def stop(self):
        return f'{self.name} остонавливается'

    def turn_right(self):
        return f'{self.name} поворачивает направо'

    def turn_left(self):
        return f'{self.name} поворачивает налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городской машины {self.name} равна {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше допустимой для городской машины'
        else:
            return f'Скорость {self.name} допустима для городской машины'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочей машины {self.name} равна {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше чем допустимая для рабочей машины'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полицейского управления'
        else:
            return f'{self.name} не из полицейского управления'


audi = SportCar(100, 'Red', 'Audi', False)
toyota = TownCar(30, 'White', 'Toyota', False)
skoda = WorkCar(70, 'Black', 'Skoda', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(skoda.turn_left())
print(f'Если {toyota.turn_right()}, тогда {audi.stop()}')
print(f'{skoda.go()} со скоростью {skoda.show_speed()}')
print(f'Цвет {skoda.name} - {skoda.color}')
print(f' {audi.name} полицейская машина? {audi.is_police}')
print(f'{skoda.name}  полицейская машина? {skoda.is_police}')
print(audi.show_speed())
print(toyota.show_speed())
print(ford.police())
print(ford.show_speed())
