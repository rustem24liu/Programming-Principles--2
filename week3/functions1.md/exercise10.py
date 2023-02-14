numbers = [int(i) for i in input().split()]
numbers2 = sorted(numbers)
res = []
def unique(numbers2):
    for i in range(len(numbers2)):
        for j in range(i):
            if numbers2[i] == numbers2[j]:
                break
        else:
            res.append(numbers2[i])
    print(res)

unique(numbers2)



# numbers = [int(i) for i in input().split()]
# result = {''}
# final = []
# def unique(numbers):
#     for x in numbers:
#         result.add(x)
#     for y in result:
#         final.append(y)
#     final.remove('')
#     print(final)
# unique(numbers)
