a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a+b)%2!=0:
    if (c+d)%2==0 and (a-1 == c and b-2 == d ) or (a+1 == c and b-2 == d) or (a+2 == c and b-1 == d) or (a+2 == c and b +1 == d) or (a+1 ==c and b+2 == d )or (a-1 == c and b+2 == d) or (a-2==c and b+1 == d )or (a -2 == c and b-1 ==d):
        print("YES")
    else:
        print("NO")
elif (a+b)%2==0:
    if (c+d)%2!=0 and (a-1 == c and b-2 == d ) or (a+1 == c and b-2 == d) or (a+2 == c and b-1 == d) or (a+2 == c and b +1 == d) or (a+1 ==c and b+2 == d )or (a-1 == c and b+2 == d) or (a-2==c and b+1 == d )or (a -2 == c and b-1 ==d):
        print("YES")
    else:
        print("NO")
