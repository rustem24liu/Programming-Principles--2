a = input()

print(a[2])
print(a[len(a)-2])
print(a[:5])
print(a[:len(a)-2])
for i in range(len(a)):
    if i%2==0:
        print(a[i], end = "")
print()
for j in range(len(a)):
    if j%2 != 0:
        print(a[j], end = "")
print()
print(a[::-1])
print(a[-1::-2])
print(len(a))