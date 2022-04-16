class Matrix():
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        item = []
        for i in range(len(self.lists)):
            item.append([])
            for j in range(len(self.lists[0])):
                item[i].append(self.lists[i][j] + other.lists[i][j])

        return Matrix(item)


matrix1 = [[31, 22], [37, 43], [51, 86]]
matrix2 = [[1, 22, 24], [6, 15, 25], [7, 21, 14]]
matrix1 = Matrix(matrix1)
matrix2 = Matrix(matrix2)
print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
print(matrix2 + matrix1)
