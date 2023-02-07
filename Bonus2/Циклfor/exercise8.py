n = int(input())
sum = 1
sum2 = 0
for i in range(n):
    sum *= (i+1)
    sum2 +=sum
    # print(sum)

print(sum2)