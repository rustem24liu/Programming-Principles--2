i = 1
n = 0
# while i !=0:
#     a = int(input())
#     if a%2 == 0 and a != 0:
#         n +=1
#     if a == 0:
#         break
# print(n)
res = []
while i != 0:
    a = int(input())
    if a%2 == 0 and a!= 0:
        res.append(a)
    if a == 0:
        break
print(len(res))