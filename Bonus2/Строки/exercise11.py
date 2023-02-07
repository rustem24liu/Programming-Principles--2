a = input()

res = a[a.index("h")+1:a.rindex("h")]
res2 = res.replace("h", "H")

print(a[:a.index("h")+1]+res2+a[a.rindex("h"):])