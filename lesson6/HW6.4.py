class Car:

    def __init__(self, speed, color, name, is_police):
        if type(speed) is int and type(color) is str \
                and type(name) is str and type(is_police) is bool:
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = is_police
            self.direction = 'прямо'
        else:
            raise TypeError('не верный тип данных')

    def show_speed(self):
        return f'текущая скорость: {self.speed}км'

    def go(self, speed):
        self.speed = speed
        return f'движется со скоростью {self.speed}км'

    def stop(self):
        self.speed = 0
        return f'стоит'

    def turn(self, direction):
        self.direction = direction
        return f'направление: {self.direction}'


class TownCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f'текущая скорость: {self.speed}км\n' \
                   f'допустимая скорость превышена'
        else:
            return f'текущая скорость: {self.speed}км\n'


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'текущая скорость: {self.speed}км\n' \
                   f'допустимая скорость превышена'
        else:
            return f'текущая скорость: {self.speed}км\n'


class SportCar(Car):

    def __init__(self):
        self.speed = 150
        self.color = 'red'
        self.name = 'sport car'
        self.is_police = False
        self.direction = 'прямо'


class PoliceCar(Car):

    def __init__(self):
        self.speed = 100
        self.color = 'blue'
        self.name = 'police car'
        self.is_police = True
        self.direction = 'прямо'

pc = PoliceCar()
print(pc.is_police)