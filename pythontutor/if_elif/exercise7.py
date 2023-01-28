a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == c and b == d-1:
    print("YES")
elif a == c and b == d+1:
    print("YES")
elif a == c+1 and b == d-1:
    print("YES")
elif a == c+1 and b == d+1:
    print("YES")
elif a == c-1 and b == d-1:
    print("YES")
elif a == c-1 and b == d+1:
    print("YES")
elif a == c-1 and b == d:
    print("YES")
elif a ==c+1 and b == d:
    print("YES")

else:
    print("NO")

"""
if a+b==c+b-2 or a+b == c+b+2 :
    print("YES")
elif a==c:
    if b==d+1 or b == d-1:
        print ("YES")
    else:
        print ("NO")
elif b==d:
    if a == c + 1 or a ==c-1:
        print ("YES")
    else :
        print("NO")
else:
    print ("NO")"""