# Write a Python program to calculate the area of a trapezoid.
import math
n = int(input("Height: "))
m = int(input("Base, first value: "))
c = int(input("Base, second value: "))

S = (m+c)/2
res = S * n
print("Area of this trapeoid is:", res)