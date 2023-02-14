
numbers = [int(i) for i in input().split()]
result = []
def spy_game(numbers):
    for x in numbers:
        if x == 0:
            result.append(x)
        elif x == 7:
            result.append(x)
    if result[0] == 0 and result[1] == 0:
        print(True)
    else:
        print(False)

spy_game(numbers)
    


# """
# def spy_game(nums):
#     pass

# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False
# """