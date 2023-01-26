list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3, 4]
list1.extend(list2)
print(list1)

list3 = ["a", "b", "c", "d"]
list4 = [1, 2, 3, 4]
for x in list4:
    list3.append(x)
print(list3)