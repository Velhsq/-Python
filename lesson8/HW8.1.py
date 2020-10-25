class MyDate:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def get_int_date(cls, date_str):
        date_str = date_str.split('-')
        day = int(date_str[0])
        month = int(date_str[1])
        year = int(date_str[2])
        date_tuple = (day, month, year)
        return date_tuple

    @staticmethod
    def date_valid(date_str):
        date_tuple = MyDate.get_int_date(date_str)
        if date_tuple[0] > 30 or date_tuple[0] < 1: #все подряд проверять не стал
            raise Exception('неверный формат')
        if date_tuple[1] > 12 or date_tuple[1] < 1:
            raise Exception('неверный формат')
        return date_tuple

print(MyDate.date_valid('01-12-2020'))



