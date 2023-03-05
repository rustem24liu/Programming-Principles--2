import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

stru = ''
for i in x:
    stru += str(i)
print(stru)