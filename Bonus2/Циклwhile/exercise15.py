n = int(input())
res = [0, 1]
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, 250):
        a, b = b, a + b
        res.append(b)
if n not in res:
    print(-1)

else:
    print(res.index(n))
