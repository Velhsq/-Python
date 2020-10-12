from random import randint


def write_random_numbers():
    file_numbers_random = []
    count = 0
    while count < 10:
        file_numbers_random.append(str(randint(0, 10)) + ' ')
        count += 1
    with open('HW5.5.txt', 'x') as a:
        a.writelines(file_numbers_random)

def file_numbers_summ():
    with open('HW5.5.txt', 'r') as a:
        numbers = a.readline()
        numbers = numbers.split()
        summ_numbers = 0
    for i in numbers:
        summ_numbers = summ_numbers + int(i)
    print(summ_numbers)

write_random_numbers()
file_numbers_summ()


