def myfunc(n):
    return lambda a: a*n
myres = myfunc(2)
print(myres(11))