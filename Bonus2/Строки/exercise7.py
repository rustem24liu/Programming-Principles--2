a = input()

res1 = a[0 : a.index("h")]
res2 = a[a.rindex("h")+1:len(a)]
print(res1+res2)
