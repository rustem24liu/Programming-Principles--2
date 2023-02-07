i = 1
res = []
maxi = -1
while i != 0:
    a = int(input())
    res.append(a)
    if maxi < a:
        maxi = a
    if a == 0:
        break
print(res.index(maxi))

