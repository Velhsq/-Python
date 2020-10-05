def my_func(x, y):
    return x ** y

def my_func2(x, y):
    count = 1
    cop_x = x
    while count != abs(y):
        x *= cop_x
        count += 1
    return 1 / x

try:
    user = input('введите действительное положительное число и целое отрицательное число через пробел\n')
    user = user.split()
    user[0], user[1] = float(user[0]), int(user[1])
    if user[1] < 0:
        print(my_func2(user[0], user[1]))
        print(my_func(user[0], user[1]))
    else:
        print('некорректный ввод')

except ValueError:
    print('некорректный ввод')


