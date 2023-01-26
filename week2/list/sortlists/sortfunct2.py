def liu(n):
    return(50-n)

newlist = [x+1 for x in range(10)]
# newlist = [1, 2 , 3, 4 ,5 ,6]
newlist.sort(key = liu)
print(newlist)
