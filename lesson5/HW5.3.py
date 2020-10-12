def staff_income():
    with open('HW5.3.txt', 'r', encoding='utf-8') as a:
        staff_lst = [line.rstrip() for line in a.readlines()]
    low_income = ''
    income_summ = 0
    count = 0
    for i in staff_lst:
        i = i.split()
        if int(i[1]) < 20000:
            low_income = low_income + i[0] + ' '
        income_summ = income_summ + int(i[1])
        count += 1
    print(f'менее 20000 зарабатывают: {low_income}')
    print(f'средний доход всех сотрудников: {income_summ/count}')


staff_income()
