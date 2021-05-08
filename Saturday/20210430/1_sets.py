## Set
## Sets are used to store multiple items in a single variable.
## Set items are unordered, unchangeable, and do not allow duplicate values.
## Once a set is created, you cannot change its items, but you can add new items.

## Duplicates Not Allowed
emptyset = {} # a set, empty
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

## Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

## Set items can be of any data type:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

## A set can contain different data types:
set1 = {"abc", 34, True, 40, "male"}

## Type
myset = {"apple", "banana", "cherry"}
print(type(myset))
print(type(list(['1', 2])))


## The set() Constructor
# set(param)
thisset = set(("apple", "banana", "cherry")) # ("apple", "banana", "cherry") is tuple 
print(thisset)

thisset = set(["apple", "banana", "cherry"]) # list
print(thisset)

thisset = set({1, "apple", 2}) # set
print(thisset)

#list, set, tuple are all iterables
# iterable : collection of elements, next() method/function to next element, return null, None