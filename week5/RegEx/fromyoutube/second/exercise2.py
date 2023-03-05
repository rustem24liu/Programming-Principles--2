
import re
from colorama import Back, Fore

s = 'r87+5616r ergklwngw-____--elkfvw wekflwe654646::+IONFEOFIELf'

result = re.search(r"\d", s)
result2 = re.findall(r'\d', s) 
result3 = re.match(r'\d', s)
print(result)
print(result2)
print(result3)

newres = re.search(r'\D', s) #! '\D' -> found firs char in the string except all numbers in the string
newres2 = re.findall(r'\D', s) #* with findall found all except all numbers 
print(newres)
print(newres2)
  
#* '\d' -> found all numbers with findall, found first known number with search, found if the number in the begin of the string