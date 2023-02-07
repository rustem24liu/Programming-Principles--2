i = 1
res = []
res1 = -1
while i!=0:
    a = int(input())
    res.append(a)
    if res1 < a:
        res1 = a
    if a == 0:
        break
res.sort()
print(res[len(res)-2])