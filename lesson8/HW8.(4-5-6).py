class MyTypeError(TypeError):
    def __init__(self, txt='Параметры неверного типа данных'):
        self.txt = txt

    def __str__(self):
        return self.txt



class Stock:
    def __init__(self, name):
        if Stock.check_str(name):
            self.name = name
            self.items_in_stock = dict({})
        else:
            raise MyTypeError


    def add_items(self, item, amount):
        if Stock.check_object(item) and Stock.check_int(amount):
            self.items_in_stock.update({item.name: amount})
            item.status = f'на складе: {self.name}'
        else:
            raise MyTypeError

    def __str__(self):
        return str(self.items_in_stock)

    @staticmethod
    def check_int(value):
        return type(value) is int

    @staticmethod
    def check_str(value):
        return type(value) is str

    @staticmethod
    def check_object(value):
        return isinstance(value, Item)


class Item:
    def __init__(self, name: str):
        self.name = name
        self.status = None


class Xerox(Item):
    def __init__(self):
        self.name = 'xerox'
        self.status = None

class Printer(Item):
    def __init__(self):
        self.name = 'printer'
        self.status = None

class Scaner(Item):
    def __init__(self):
        self.name = 'scaner'
        self.status = None


s = Stock('stock_1')
s_1 = Stock('stock_2')
it_1 = Xerox()
it_2 = Scaner()
it_3 = Printer()
s.add_items(it_3, 5)
s.add_items(it_1, 3)
print(it_3.status)
print(s)
