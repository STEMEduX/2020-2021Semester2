# Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
# for e in tropical:
#     thislist.append(e)

# ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya'] ?
# 6 elements
# thislist.append(tropical) 
# ['apple', 'banana', 'cherry', ['mango', 'pineapple', 'papaya']]
# 4 elements, but last element has 3 children
print(thislist)

# Add Any Iterable, tupe, any list, any array, any set, any collection
# iterable, next()
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange") # (key, value)  (id, name, age, score)
thislist.extend(thistuple)
print(thislist)

# # Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana"]
# thislist.remove("bananA") # error list.remove(x): x not in list
if "bananA" in thislist:
    thislist.remove("bananA")
print(thislist)

# # Remove Specified Index
thislist = ["apple", "banana", "cherry"]
deleted = thislist.pop(1)
print(thislist)
print(deleted)

requests = [1, 2, 3, 4]
while requests:
    cur = requests.pop(0)
    print('processing ' + str(cur))

thislist = ["apple", "banana", "cherry"]
deleted = thislist.pop()
print(thislist)
print(deleted)

# # del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist) # name 'thislist' is not defined

# # Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
