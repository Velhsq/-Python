count = 1
lst = []
user = input('Введите название, цену, количество, единицы через пробел: ')
while user:
    user = user.split()
    new_dct = {
        "название": user[0],
        "цена": int(user[1]),
        "количество": int(user[2]),
        "единицы": user[3]
    }
    lst.append((count, new_dct))
    count += 1
    user = input('Введите название, цену, количество, единицы через пробел: ')

print(lst)

result = {
    "название": [],
    "цена": [],
    "количество": [],
    "единицы": set()
}
for i in lst:
    result.get('название').append(i[1].get('название'))
    result.get('цена').append(i[1].get('цена'))
    result.get('количество').append(i[1].get('количество'))
    result.get('единицы').add(i[1].get('единицы'))



print(result)






