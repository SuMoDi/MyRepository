# easy_map
def normalize(name):
    return name[0].upper() + name[1:].lower()

L = ['adam', 'LISA', 'barT']
print (list(map(normalize,L)))

# easy_reduce
from functools import reduce
def ji(x,y):
    return x*y

def prod(L):
    return reduce(ji,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
