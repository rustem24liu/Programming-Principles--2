a = input()

print(a.index("f"), end = " ")

res = a.count("f")
if res > 1:
     print(a.rindex("f"))