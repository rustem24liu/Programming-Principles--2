def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
myfourthler = myfunc(4)

print(mydoubler(11))
print(mytripler(11))
print(myfourthler(11))
