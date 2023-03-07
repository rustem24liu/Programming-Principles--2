
def my2():
    cnt = 0
    cnt1 = 0
    string = input()
    for i in range(len(string)):
        if string[i].islower():
            cnt+=1
        if string[i].isupper():
            cnt1+=1
    print("Upper letters' number is: "+str(cnt1))
    print("LOwer letters' number is: "+str(cnt))

my2()