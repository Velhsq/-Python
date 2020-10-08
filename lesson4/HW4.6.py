from itertools import count, cycle

for el in count(3):
    if el > 5:
        break
    else:
        print(el)


lst = ['f', 2, 'o']



counter = 0
for el in cycle(lst):
    if counter >= 5:
        break
    else:
        print(el)
    counter += 1
