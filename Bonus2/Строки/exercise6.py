a = input()

res = a.count("f")
if res == 1:
    print("-1")
elif res == 0:
    print("-2")
# else:
#     res2 = a[a.index("f")+1:]
#     res3 = a[:a.index("f")]
#     res4 = res3+res2
#     print(res4.index("f")+1) 

else:
    print(a.find("f", a.index("f")+1))
    print(a.find("f", a.index("f")+1, len(a)))