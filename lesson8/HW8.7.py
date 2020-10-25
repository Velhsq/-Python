class ComplexNumbers:
    def __init__(self, number):
        if ComplexNumbers.check_complex_number(number):
            self.number = number
        else:
            raise TypeError

    def __add__(self, other):
        if isinstance(other, ComplexNumbers):
            return self.number + other.number
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, ComplexNumbers):
            return self.number * other.number
        else:
            raise TypeError

    @staticmethod
    def check_complex_number(value):
        return type(value) is complex

cn_1 = ComplexNumbers(3 + 2j)
cn_2 = ComplexNumbers(2 + 3j)
print(cn_1 + cn_2)
print(cn_1 * cn_2)