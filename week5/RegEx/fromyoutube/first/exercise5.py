import re

s = 'AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'

result = re.sub('A', 'D',  s) #! sub -> replaces the string to another 

print(result)