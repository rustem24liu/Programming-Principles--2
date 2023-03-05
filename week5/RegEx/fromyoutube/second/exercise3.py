import re

s = 'r87+ 5616r ergklwngw-____ --elkfvw wekflwe654646::+IONFEOFIELf'

result = re.search(r'\s', s) #! '\s' -> find all signs 
result = re.findall(r'\s', s)
print(result)