n = int(input())
b = {''}
d = {''}
if n == 1:
    print(1)
elif n != 1:
    for j in range(1, n+1):
        d.add(j)

    for i in range(1, n):
        a = int(input())
        b.add(a)
        c = d.difference(b)
    for k in c:
        print(k)
