a = [5, 2, 's', 4.5, 4, (5, 7), 'r', 2, 5]


for i in range(len(a)):
    if i % 2 != 0:
        a[i - 1], a[i] = a[i], a[i - 1]

print(a)