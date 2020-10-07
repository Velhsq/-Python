from sys import argv

def salary(working=float(argv[1]), hours=float(argv[2]), prize=float(argv[3])):
    return working * hours + prize

try:
    print(salary())
except ValueError:
    print('не верный ввод')