# Python Lists


# Lists are used to store multiple items in a single variable.
# collections : list, set, tuple, dictionary


# thislist = ["apple", "banana", "cherry"]
# print(thislist)


# index access

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list



# Changeable/Mutable
# The list is changeable, meaning that we can change, add, and remove items 
# in a list after it has been created.



# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:


# List Length
# To determine how many items a list has, use the len() function:


# List Items - Data Types
# List items can be of any data type, can mix different data types


# type()


# The list() Constructor
# list("asdfasdf")

# Access Items
# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

# Negative Indexing
# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

# Range of Indexes
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# print(thislist[:4])
# print(thislist[2:])
# print(thislist[-4:-1])

# Check if Item Exists
# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# Change Item Value
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# Change a Range of Item Values
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# Insert Items
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)