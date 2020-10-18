class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'запуск отрисовки ({self.title})')


class Pen(Stationery):

    def __init__(self):
        self.title = 'pen'

    def draw(self):
        print(f'запуск письма ({self.title})')


class Pencil(Stationery):

    def __init__(self):
        self.title = 'pencil'

    def draw(self):
        print(f'запуск черчения ({self.title})')


class Handle(Stationery):

    def __init__(self):
        self.title = 'handle'

    def draw(self):
        print(f'запуск замазывания ({self.title})')


hndl = Handle()
hndl.draw()