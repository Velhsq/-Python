while True:
    try:
        user_number = int(input('введите номер месяца: '))
        if user_number < 1 or user_number > 12:
            print('вы ввели некорректное число')
            continue
    except ValueError:
        print('некорректный ввод')
    else:
        break

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]


if user_number in winter:
    print('winter')
elif user_number in spring:
    print('spring')
elif user_number in summer:
    print('summer')
elif user_number in autumn:
    print('autumn')


seasons = {'winter': [12, 1, 2],
           'spring': [3, 4, 5],
           'summer': [6, 7, 8],
           'autumn': [9, 10, 11]
           }

for i in seasons.items():
    if user_number in i[1]:
        print(i[0])
        break
