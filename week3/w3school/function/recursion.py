def tri_recursion(k):
    if(k == 0):
        res = 0
        return res
    elif(k > 0):
        res = k + tri_recursion(k-1)
        return res
print(tri_recursion((int(input()))))