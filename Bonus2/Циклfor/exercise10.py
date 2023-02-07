n = int(input())
# sum1 = ""
# for i in range(n):
#     sum1 +=str(i+1)
#     print(sum1)


for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, sep = " ", end = "")
    print()
