## join
## +
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
list4 = list2 + list1
print(list3)
print(list4)

## append
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
# list1.append(list2) # ['a', 'b', 'c', [1,2,3]]
for x in list2:
  list1.append(x)

print(list1)

## extend
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)