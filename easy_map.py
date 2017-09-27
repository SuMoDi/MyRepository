def normalize(name):
    return name[0].upper() + name[1:].lower()

L = ['adam', 'LISA', 'barT']
print (list(map(normalize,L)))
