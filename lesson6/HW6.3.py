class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        return full_name

    def get_total_income(self):
        full_income = self._income.get('wage') + \
                      self._income.get('bonus')
        return full_income

ivan = Position('ivan', 'ivanov', 'klerk', 100, 500)

print(ivan.get_full_name())
print(ivan.get_total_income())
