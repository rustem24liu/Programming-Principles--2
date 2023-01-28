n = int(input())
m = int(input())
k = int(input())

sumk = n*m
if sumk >= k:
    if k % n == 0 or k % m == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")