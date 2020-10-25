class StringTypeInputError(Exception):
    def __init__(self, txt='вводимые данные должны быть числами'):
        self.txt = txt

    def __str__(self):
        return self.txt


lst_numbers = []
while True:
    user_input = input('вводите числа\n'
                       'для завершения работы введите "stop"\n')
    if user_input == 'stop':
        break
    try:
        if not user_input.isdigit():
            raise StringTypeInputError
        user_input = user_input.split()
        for i in user_input:
            lst_numbers.append(i)
    except StringTypeInputError as er:
        print(er)

if lst_numbers:
    print(''.join(lst_numbers))
else:
    print('вы ничего не ввели')




