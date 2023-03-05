import re

s = '87+5616r ergklwngw -____--elkfvw wekflwe654646::+IONFEOFIELf'

result = re.search(r'e...k', s) # '.' точка найдет пропущенное char or string

print(result)
