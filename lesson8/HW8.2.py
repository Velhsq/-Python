class MyError(Exception):
    def __init__(self, txt='Деление на ноль!'):
        self.txt = txt

    def __str__(self):
        return self.txt

try:
    a = int(input('1/x: введите x '))
    if a == 0:
        raise MyError
except MyError as mr:
    print(mr)

