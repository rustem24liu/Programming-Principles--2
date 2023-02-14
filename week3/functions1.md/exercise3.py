# x-> chicken
# y-> rabbit
def rabbitsandchicken(numhead, numlegs):
    y = 2*numhead-numlegs/2
    x = numhead - y
    return int(x) , int(y)
# print(rabbitsandchicken(35, 94))