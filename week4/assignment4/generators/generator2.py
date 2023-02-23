n = int(input())
result = []
for i in range(n):
    if i % 2 == 0:
        result.append(i)
res = str(result)
x = res.replace('[', '')
y = x.replace(']', '')
print(y+'.')
