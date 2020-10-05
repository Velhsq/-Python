def data(name, surname, birthday, city, email, telephone_number):
    print(f'имя: {name}, фамилия: {surname}, дата рождения: {birthday}\n'
          f'город проживания: {city}, email: {email}, номер телефона: {telephone_number}')

user = input('введите через пробел имя, фамилию, дату рождения, город проживания, '
             'email, номер телефона\n')
user = user.split()
if len(user) == 6:
    data(name=user[0], birthday=user[2], surname=user[1], city=user[3], telephone_number=user[5], email=user[4])
else:
    print('некорректный ввод')