import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1) #! the last parametr in this scope is the mean of maxsplit
print(x)

new =''
for i in x:
    new += i

print(new)
