import re

s = 'AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'
 
result = re.findall('DC', s) # -> add all finding strings to the list

print(result)