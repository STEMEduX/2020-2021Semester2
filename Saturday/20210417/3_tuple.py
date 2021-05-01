## Python - Update Tuples
## Change Tuple Values
## Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
## But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
# x[1] = "kiwi"
y = list(x)
y[1] = "kiwi" # change list
x = tuple(y) # construct the tuple back.
print(x)

## Add Items
## Once a tuple is created, you cannot add items to it.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

## Remove Items
# thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

## The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
# tuple does not have clear, since it is unchangable.
# print(thistuple) #this will raise an error because the tuple no longer exists

## clear vs del
thislist = [1, 2, 3, 4]
thislist.clear() # delete all the elements in the list
print(thislist)

del thislist
print(thislist) # name 'thislist' is not defined
