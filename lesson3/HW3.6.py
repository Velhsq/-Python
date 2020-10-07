def text_change(a):
    return a.title()

user = input('вводите слова через пробел\n')
while user:
    print(text_change(user))
    user = input('вводите слова через пробел\n')


