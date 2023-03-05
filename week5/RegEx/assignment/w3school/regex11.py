import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span()) #! span -> returns the position on the set (first position, the last position)
print(x)

