a = input()
res1 = a[a.index("h")+1:a.rindex("h")]
res2 = res1[::-1]
print(a[:a.index("h")+1]+res2+a[a.rindex("h"):])