class Cell:
    def __init__(self, number: int):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        if self.number >= other.number:
            return self.number - other.number
        else:
            return print('вычитаемое меньше вычитателя')

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return round(self.number / other.number)

    @staticmethod
    def make_order(other, row):
        number = other.number
        count = 0
        row_count = 0
        lst = []
        while count < number:
            if row_count == row:
                lst.append('\n')
                row_count = 0
            else:
                lst.append('1')
                count += 1
                row_count += 1
        return ''.join(lst)





cell_1 = Cell(10)
cell_2 = Cell(16)
print(cell_1 + cell_2)

print(cell_1 - cell_2)
print(cell_2 - cell_1)

print(cell_1 * cell_2)

print(cell_1 / cell_2)

print(Cell.make_order(cell_2, 5))