from datetime import date , timedelta

print("Today's date:", date.today())
x = date.today()-timedelta(5)
print("The day before 5 day:", x)