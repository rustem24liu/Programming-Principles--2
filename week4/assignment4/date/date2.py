from datetime import date , timedelta

yesterday = date.today() - timedelta(1)
print("Yesterday was:", yesterday)
today = date.today()
print("Today is:", today)
tomorrow = date.today()+timedelta(1)
print("Tomorrow will be:", tomorrow)