def user_input():
    user = input('построчно вводите данные\n')
    user_strings = []
    while user:
        user_strings.append(user + '\n')
        user = input('построчно вводите данные\n')
    return user_strings


with open('HW5.1.txt', 'a') as a:
    a.writelines(user_input())
