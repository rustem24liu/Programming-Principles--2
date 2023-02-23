from colorama import Fore , Back
import datetime
from datetime import time

print(Fore.GREEN)
print("You should write date like this:", Fore.RED, datetime.datetime.today())
print(Fore.GREEN)
x = int(input("YEAR-> "))
y = int(input("MONTHS-> "))
z = int(input("DAY-> "))
x2 = int(input("SECOND YEAR-> "))
y2 = int(input("SECOND MONTHS-> "))
z2 = int(input("SECOND DAY-> "))

res = datetime.date(x, y, z)
res2 = datetime.date(x2, y2, z2)
day = (abs(res - res2)).days *24*60*60

print(Fore.YELLOW+"The total second between this dates is:", Fore.RED,day)










