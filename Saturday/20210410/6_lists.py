## Copy 
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist
# thislist.append("new")
# print(thislist)
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# thislist.append("new")
# print(thislist)
# print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
thislist.append("new")
print(thislist)
print(mylist)
