a = int(input())
b = int(input())
c = int(input())
d = int(input())

sum1 = a+b
sum2 = c+d
if sum1 % 2 == 0 and sum2 % 2 == 0 or sum1 % 2 !=0 and sum2 % 2 !=0:
    #sum1 % 2 == sum2 %2
    print("YES")
else:
    print("NO")