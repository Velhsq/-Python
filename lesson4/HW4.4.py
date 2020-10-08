
# 1 решение: через метод списка count
lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
def generator(a):
    for i in a:
        if a.count(i) == 1:
            yield i
print([el for el in generator(lst)])


# 2 решение: по счетчику
lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
def generator2(a):
    for i in a:
        count = 0
        for x in a:
            if i == x:
                count += 1
            if count > 1:
                break
        if count == 1:
            yield i
print([el for el in generator2(lst)])


# 3 решение: по длине генерируемых списков
lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
def generator3(a):
    for i in a:
        b = [el for el in a if i == el]
        if len(b) == 1:
            yield int(i)
print([el for el in generator3(lst)])