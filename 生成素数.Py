l = list(range(3,100))

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = iter(l)
    it = filter(_not_divisible(2),it)
    try:
      while True:
          n = next(it)
          yield n
          it = filter(_not_divisible(n),it)
    except StopIteration as e:
         print ('Generator return value:',e.value)
        
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
