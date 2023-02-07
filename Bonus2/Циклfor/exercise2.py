a = int(input())
b = int(input())



if a > b:
    for i in range(a, b-1, -1):
        print(i, end = " ")


elif a < b:
    for r in range(a, b+1,1):
        print(r, end = " ")

else:
    print(a)