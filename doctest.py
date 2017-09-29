def fact(n):
    '''
    
    jiecheng
    
    >>> fact(1)
    1
    >>> print('-------------------')
    >>> a = fact(2)                       #>>>和a之间必须有空格
    >>> a
    2
    >>> a = fact(3)
    >>> a
    6
    >>> a = fact(4)
    >>> a
    24
    >>> print('-------------------')
    >>> a = fact(-1)
    >>> a 
    Traceback (most recent call last):
        ...
    ValueError: 'fact' can not deal with a
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n-1)
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
