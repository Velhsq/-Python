def read_file():
    with open('HW5.6.txt', 'r', encoding='utf-8') as a:
        file_text = a.readlines()
    lessons_dict = dict()
    for i in file_text:
        i = i.split()
        name = i[0][:-1]
        i.pop(0)
        count = -3
        lessons_hours = 0
        for x in i:
            try:
                lessons_hours = lessons_hours + int(x[:count])
                count -= 1
            except ValueError:
                count -= 1
                continue

        lessons_dict.update({name: lessons_hours})
    print(lessons_dict)








read_file()
