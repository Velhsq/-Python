rating = [5, 7, 8, 9, 10, 6]



count = 0
while count < 5:
    try:
        user = int(input('Укажите рейтинг от 1 до 10: '))
        if user < 1 or user > 10:
            print('некорректное число')
            continue
    except ValueError:
        print('некорректный ввод')
    else:
        rating.append(user)
        rating = sorted(rating, reverse=True)
        print(rating)
        count += 1

