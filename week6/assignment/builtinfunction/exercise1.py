

def my(list):
    result = 1
    list = [int(i) for i in input().split()]
    for x in list:
        result = result * x
    print(result)

my(list)

#! another way with built in function math.prod
import math
anotherlist = [int(i) for i in input().split()]
product = math.prod(anotherlist)
print(product)