import math

n = int(input("Input number of sides: "))
s = int(input("Input the length of a side: "))

if n == 3:
    p = (n*s)/2
    S = p*(p-s)*(p-s)*(p-s)
    res = math.sqrt(S)
    print("Area of triangle is:", res)
elif n == 4:
    p = s*s
    print("Area of rectangle is:", p)

else:
    res = (n * s**2)/ (4 * (math.tan(math.pi/n)))
    print("Area of the regular polygon:", int(res))
