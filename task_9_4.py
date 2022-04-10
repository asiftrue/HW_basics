class Car:
    is_police = False
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        # self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала.'

    def stop(self):
        return f'Машина {self.name} остановилась.'

    def turn(self, direction):
        if direction == 1:
            return f'Машина {self.name} повернула налево.'
        elif direction == 2:
            return f'Машина {self.name} повернула направо.'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч. \n'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            a = self.speed - 60
            return f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч. Превышение скорости на {a} км/ч.\n'
        else:
            return f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч.\n'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            a = self.speed - 40
            return f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч. Превышение скорости на {a} км/ч. \n'
        else:
            return f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч.\n'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name)


town_car = TownCar(65, 'черный', 'Opel')
print(f'Марка: {town_car.name}')
print(f'Цвет: {town_car.color}')
print(f'Полицейская: {town_car.is_police}')
print(town_car.go())
print(town_car.turn(2))
print(town_car.stop())
print(town_car.show_speed())

print('Компактный вывод')
sports_car = SportCar(100, 'красный', 'McQueen')
print(f'Марка: {sports_car.name}, цвет: {sports_car.color}, полицейская: {sports_car.is_police}')
print(f'{sports_car.go()} {sports_car.turn(2)} {sports_car.stop()} {sports_car.show_speed()}') # работает только если аргумент turn() число
# print(f'{sports_car.turn('направо')}') # не работает, ищет скобку :(
# print(sports_car.go())
# print(sports_car.stop())
# print(sports_car.show_speed())

work_car = WorkCar(62, 'зеленый', 'Komatsu')
print(f'Марка: {work_car.name}')
print(f'Цвет: {work_car.color}')
print(f'Полицейская: {work_car.is_police}')
print(work_car.go())
print(work_car.turn(1))
print(work_car.stop())
print(work_car.show_speed())

police_car = PoliceCar(70, 'черный', 'Ford')
print(f'Марка: {police_car.name}')
print(f'Цвет: {police_car.color}')
print(f'Полицейская: {police_car.is_police}')
print(police_car.go())
print(police_car.turn(1))
print(police_car.stop())
print(police_car.show_speed())
