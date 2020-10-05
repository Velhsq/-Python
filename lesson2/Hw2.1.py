a = [(1, 2), 1, 'a', 3.1, True, {1: 2, 'a': 'b'}, ['c', 3.5, [1, 2]]]

for i in a:
    print(type(i))
    if type(i) is tuple or type(i) is set or type(i) is list or type(i) is dict:
        for x in i:
            print(f'    вложенный тип данных: {type(x)}')


