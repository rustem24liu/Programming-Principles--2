i = 1
cnt = 0
res = []
while i != 0:
    a = int(input())
    res.append(a)
    if a == 0:
        break
for x in range(len(res)):
    if res[x]>res[x-1]:
        cnt+=1

print(cnt-1)