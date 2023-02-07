import math
a = int(input())
i = 0
while(i < a):
    i+=1
    if int(math.sqrt(i))*int(math.sqrt(i)) == i:
        print(i, end = " ")
    