i = 1
sum = 0
n = 0
while i != 0:
    a = int(input())
    sum += a
    n += 1
    if a == 0:
        break
res = sum/(n-1)

print(res)