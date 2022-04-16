class Cell():
    def __init__(self, slot_no):
        self.slot_no = slot_no

    def make_order(self, row_len: int):
        items = '*' * self.slot_no
        rows = [
            items[idx:idx + row_len]
            for idx in range(0, len(items), row_len)
        ]
        return '\n'.join(rows)

    def __str__(self):
        return f'{self.slot_no}'

    def __add__(self, other):
        print()
        return Cell(self.slot_no + other.slot_no)

    def __sub__(self, other):
        print()
        if self.slot_no < other.slot_no:
            raise ValueError("Pазность количества ячеек двух клеток должна быть больше нуля")
        return Cell(self.slot_no - other.slot_no)

    def __mul__(self, other):
        print()
        return Cell(self.slot_no * other.slot_no)

    def __floordiv__(self, other):
        print()
        return Cell(self.slot_no // other.slot_no)


cell1 = Cell(16)
cell2 = Cell(22)
print(cell2.make_order(5))
print(cell1 + cell2)
# print(cell1 - cell2) # исключение
print(cell2 - cell1)
print(cell1 * cell2)
print(cell1 // cell2)
