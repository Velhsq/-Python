def file_change():
    with open('HW5.4(eng).txt', 'r', encoding='utf-8') as a:
        file_eng = [line.rstrip() for line in a.readlines()]
    file_rus = []
    for i in file_eng:
        i = i.split()
        if i == []:
            continue
        elif i[0] == 'One':
            i[0] = 'Один'
        elif i[0] == 'Two':
            i[0] = 'Два'
        elif i[0] == 'Three':
            i[0] = 'Три'
        else:
            i[0] = 'Четыре'
        i.append('\n\n')
        i = ' '.join(i)
        file_rus.append(i)
    with open('HW5.4(rus).txt', 'w', encoding='utf-8') as a:
        a.writelines(file_rus)



file_change()











