
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style

print(Fore.RED)
print( Back.GREEN)  
atfirst = input("What you want? (+, -, *, /, %): " )
print(Back.CYAN)


a = float(input("first number: "))
b = float(input("second number: "))
print(Style.RESET_ALL)
print(Back.WHITE)
if atfirst == "+":  
    print(a+b)
elif atfirst == "-":
    print(a-b)
elif atfirst == "*":
    print(a*b)
elif atfirst == "/":
    print(a/b)
elif atfirst == "%":
    print(a%b)
else:
    print("invalid status")
