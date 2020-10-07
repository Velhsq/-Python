from itertools import count
from functools import reduce
def fact(n):
    a = []
    for i in count(1):
        if i > n:
            break
        a.append(i)
    yield reduce(lambda x, y: x * y, a)



print([el for el in fact(5)])





