user = input('Введите несколько слов через пробел: ')

user = user.split()
for i in enumerate(user, 1):
    i = list(i)
    i[0] = str(i[0])
    if len(i[1]) > 10:
        i[1] = i[1][:10]
    print(') '.join(i))


