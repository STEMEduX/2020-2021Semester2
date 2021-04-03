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
print(thislist)

# Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
