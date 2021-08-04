import time


class TrafficLight:
    __color = 'red'

    def running(self):
        print('Светофор работает')

        self.__color = 'Красный'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(7)

        self.__color = 'Желтый'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(2)

        self.__color = 'Зеленый'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(5)

        while True:
            self.running()


traff_light = TrafficLight()
print(traff_light.running())
