import copy
class Matrix:
    def __init__(self, numbers):
        len_numbers = numbers[0]
        for i in numbers:
            if len(len_numbers) != len(i):
                raise Exception('разная длина вложенных списков')
            len_numbers = i
        self.numbers = numbers

    def __str__(self):
        for i in self.numbers:
            print(i)
        print('\n')

    def __add__(self, other: object):
        copy_numbers = copy.deepcopy(self.numbers)
        count_1 = 0
        if len(self.numbers) == len(other.numbers):
            while count_1 < len(copy_numbers):
                count_2 = 0
                if len(self.numbers[count_1]) == len(other.numbers[count_1]):
                    while count_2 < len(copy_numbers[count_1]):
                        copy_numbers[count_1][count_2] += other.numbers[count_1][count_2]
                        count_2 += 1
                    count_1 += 1
                else:
                    raise Exception('несоответвие матриц')
        else:
            raise Exception('несоответвие матриц')
        for i in copy_numbers:
            print(i)
        print('\n')
        return Matrix(copy_numbers)


m_1 = Matrix([[1, 2, 3], [2, 2, 3]])
m_2 = Matrix([[2, 3, 4], [2, 3, 4]])

m_1.__str__()
m_2.__str__()
m_1.__add__(m_2)
m_2.__add__(m_1)
