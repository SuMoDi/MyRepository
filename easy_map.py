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


# use map and reduce to change str to float
from functools import reduce
def str2float(s):
    pos = s.find('.')
    def str2int(s):
        l = [ int(x) if x in '1234567890' else x for x in s]
        print (l)
        return l
    def float1(s):
        pass
    
    def int2float(s):
        #pos = s.find('.')
        num1 = reduce(lambda x,y: x*10 + y,s[0:pos])
        print (num1)
        l = s[(pos+1):]
        l.reverse()
        print(l)
        num2 = reduce(lambda x,y: x/10+y,l)
        print (num2)
        return num1+num2/10
    return int2float(str2int(s))

print('str2float(\'123.456\') =', str2float('123.456'))
