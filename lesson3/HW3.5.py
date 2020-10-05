def sum_numbers(a):
    numbers = []
    for i in a:
        i = float(i)
        numbers.append(i)
    return sum(numbers)


past_summ = 0
while True:
    try:
        user = input('вводите числа через пробел, чтобы выйти введите "!"\n')
        user = user.split()
        past_summ = past_summ + sum_numbers(user)
        print(past_summ)
    except ValueError:
        if '!' in user:
            while '!' in user:
                user.remove('!')
            print(past_summ + sum_numbers(user))
            break
        else:
            print('некорректный ввод')