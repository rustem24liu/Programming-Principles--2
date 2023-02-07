n = int(input())
i = 1
res = 1
while 2**i <= n:
    res = 2**i
    i+=1
print(i-1, res)

