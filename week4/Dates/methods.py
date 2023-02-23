import datetime
# name = input("Your name, Please? ")
# print("Hello,", name , "we can find exact date, that your write")

year = int(input("year? "))
month = int(input("month? "))
day = int(input("day? "))

x = datetime.datetime(year, month, day)

print("it was->", x.strftime("%A"))
print("in short->", x.strftime("%a"))
print("month->", x.strftime("%B"))
print("monthshort->", x.strftime("%b"))
# print("monthshort->", x.strftime("%С"))


