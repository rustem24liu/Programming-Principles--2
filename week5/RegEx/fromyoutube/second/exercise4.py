import re

s = 'r87+5616r ergklwngw-____--elkfvw wekflwe654646::+IONFEOFIELf'

result = re.search(r'\bwek', s) 
result = re.search(r'\d*', s) 
result2 = re.findall(r'\d+', s) 
print(result)
print(result2)