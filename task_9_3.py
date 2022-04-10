class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'ФИО: {self.name} {self.surname}'

    def get_total_income(self):
        a = self._income['wage'] + self._income['bonus']
        return f'Доход: {a}'
        # return f'Доход: {sum(self._income.values())}'


pos1 = Position('Иван', 'Петров', 'Экономист', 100000, 50000)
# print(pos1.name)
# print(pos1.surname)
# print(pos1.position)
# print(pos1._income)
print(pos1.get_full_name())
print(pos1.get_total_income())
pos2 = Position('Елена', 'Иванова', 'Бухгалтер', 90000, 30000)
print(pos2.get_full_name())
print(pos2.get_total_income())