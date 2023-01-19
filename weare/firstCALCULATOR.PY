# firs calculator

atfirst = input("What you want? (+, -): " )

a = int(input("first number: "))
b = int(input("second number: "))

if atfirst == "+":  
    print(a+b)
elif atfirst == "-":
    print(a-b)
else:
    print("invalid status")