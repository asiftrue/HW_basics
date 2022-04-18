class ComplexNum:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f'{self.a}'

    def __add__(self, other):
        return ComplexNum(self.a + other.a)

    def __mul__(self, other):
        return ComplexNum(self.a * other.a)


z1 = ComplexNum(complex(1, 1))
z2 = ComplexNum(complex(2, 4))

print(z1)
print(z2)
print(z1 + z2)
print(z1 * z2)
