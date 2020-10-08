def fact(n):
    prev_numbers = 1
    for i in range(1, n + 1):
        yield i * prev_numbers
        prev_numbers = i * prev_numbers


for el in fact(6):
    print(el)


