n = int(input())
n = n%(24*60)
hour = n // 60
minut = abs(hour*60-n)
print(hour)
print(minut)