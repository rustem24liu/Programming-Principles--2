import json

#-> some JSON:
x = '{ "name":"rustem" , "age":17, "city":"Uralsk"}'

y = json.loads(x)

print(y)