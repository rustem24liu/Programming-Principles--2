import re

s = 'AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'

result = re.match('AC', s) #! match -> search and find substring in the begin of the string
result2 = re.match('DC', s) # if not -> return None 

print(result)
print(result2)
