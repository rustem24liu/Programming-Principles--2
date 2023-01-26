list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list3 = ["a", "b" , "c"]
list4 = [1, 2, 3]
list3.extend(list4)
print(list3)

# for x in list2:
#     list1.append(x) 