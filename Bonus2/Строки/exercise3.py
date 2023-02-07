import math

a = input()
b = math.ceil(len(a)/2)
res1 = a[b:]
res2 = a[:b]
print(res1+res2)

