lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

def generator(a):
    b = a[0]
    for i in a:
        if i > b:
            yield i
        b = i

print([el for el in generator(lst)])