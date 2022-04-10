class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print('Запуск рисования ручкой')


class Pencil(Stationary):
    def draw(self):
        print('Запуск рисования карандашом')


class Handle(Stationary):
    def draw(self):
        print('Запуск рисования маркером')


pen = Pen('Ручка')
pen.draw()
pencil = Pencil('Карандаш')
pencil.draw()
handle = Handle('Маркер')
handle.draw()
