l = [909,1001,232,99991,9898,9889]
def filt(n):
    str_n = str(n)
    n = len(str_n)
    i = 0
    flag = True
    while i<(n/2):
        if str_n[i] != str_n[-1-i]:
            flag = False
        i += 1
    return flag

x = filter(filt,l)
for i in x:
    print(i)
