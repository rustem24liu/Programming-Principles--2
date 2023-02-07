i = 1
res = -1
while i !=0:
    a = int(input())
    if res < a:
        res = a
    elif a == 0:
        break
print(res)
