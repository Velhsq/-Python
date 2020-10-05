def division(a, b):
    return a / b

def request():
    return input('введите через пробел делимое число и делитель: ')

user = request()

while user:
    try:
        user = user.split()
        if len(user) == 2:
            dividend = float(user[0])
            divider = float(user[1])
            print(division(dividend, divider))
            user = request()
        else:
            print('некорректный ввод')
            user = request()
    except ValueError:
        print('некорректный ввод')
        user = request()
    except ZeroDivisionError:
        print('деление на ноль!')
        user = request()



