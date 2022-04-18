class MyErr(Exception):
    pass


class Warehouse:
    items = {}
    detailed_items = []


class Appliances:
    def __init__(self, year, serial, name):
        self.year = year
        self.serial = serial
        self.name = name

    def __str__(self):
        return f'Наименование: {self.__class__.__name__} {self.name}, год выпуска: {self.year}, серийный номер: {self.serial}'

    def to_w(self):
        key = self.__class__.__name__
        if key not in Warehouse.items:
            Warehouse.items[key] = 1
            Warehouse.detailed_items.append(
                (f'\n  * Тип: {self.__class__.__name__}, модель: {self.name}, с/н: {self.serial}'))
        else:
            Warehouse.items[key] += 1
            Warehouse.detailed_items.append(
                (f'\n  * Тип: {self.__class__.__name__}, модель: {self.name}, с/н: {self.serial}'))
        return f'{Warehouse.items}: {"".join(Warehouse.detailed_items)}'

    def from_w(self):
        key = self.__class__.__name__
        try:
            if key in Warehouse.items:
                Warehouse.items[key] -= 1
                Warehouse.detailed_items.remove(
                    (f'\n  * Тип: {self.__class__.__name__}, модель: {self.name}, с/н: {self.serial}'))
            else:
                raise MyErr('Оргтехника такого типа отсутствует на складе.')
        except MyErr as err:
            print(err)

        if Warehouse.items[self.__class__.__name__] == 0:
            Warehouse.items.pop(self.__class__.__name__)
        return f'{Warehouse.items}: {"".join(Warehouse.detailed_items)}'


class Printer(Appliances):
    def __init__(self, year, serial, name, colour=False):
        super().__init__(year, serial, name)
        self.colour = colour


class Scanner(Appliances):
    def __init__(self, year, serial, name, resolution):
        super().__init__(year, serial, name)
        self.resolution = resolution


class Xerox(Appliances):
    def __init__(self, year, serial, name, speed):
        super().__init__(year, serial, name)
        self.speed = speed


prtr1 = Printer(2019, '213155', 'HP250', True)
prtr2 = Printer(2021, '121-55-88', 'HP80', True)
scnr1 = Scanner(2020, '51656', 1600, 'CanoScan')
xrx1 = Xerox(2018, '12-251', 110, 'B205')

print(f'Вся оргтехника: \n- {prtr1},\n- {prtr2},\n- {scnr1},\n- {xrx1}')
# Отправляем на склад
print(f'Оргтехника на складе: {prtr1.to_w()}')
print(f'Оргтехника на складе: {prtr2.to_w()}')
print(f'Оргтехника на складе: {xrx1.to_w()}')
print(f'Оргтехника на складе: {scnr1.to_w()}')

# Забираем со склада
print(f'Оргтехника на складе: {scnr1.from_w()}')

# Пробуем забрать со склада то, чего нет
print(f'Оргтехника на складе: {scnr1.from_w()}')
