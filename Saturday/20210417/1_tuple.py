## Tuple
## Tuples are used to store multiple items in a single variable.
## Tuple is one of 4 built-in data types in Python used to store 
## collections of data, the other 3 are List, Set, and Dictionary, 
## all with different qualities and usage.
## A tuple is a collection which is ordered and unchangeable.
## Tuples are written with round brackets.

# 2D point (x, y) -> x, y related data
# 3D point (x, y, z) 
# nD point (x1, .... xn)
# (No, first, last, grade, score), related
# group data => data struct, operate the struct as whole
# class, tuple java, C#
# old version python < 2.6, 2.7, limit < 20x elements in tuple
# python 3, unlimit


## Tuple items are ordered, unchangeable, and allow duplicate values.
## struture is ordered you can access it by index
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
student = (12, "james", "bond", 6, 99.9, 99.9) # student in tuple
print(thistuple)
print(thistuple[0], "---", thistuple[2])
thislist[0] = "again"
# thistuple[0] = "again" # error: 'tuple' object does not support item assignment

## length
print('---------')
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

## Tuple With One Item
print('---------')
thisbadTuple = ("apple") # expression, result is a value. unpack and get a string vaule
thistuple = ("apple",) # tuple.
print(type(thisbadTuple))
print(type(thistuple))
print(thistuple[0])

## compare list and tuple
## all ordered can access by index
## all allow duplicate values

## changable vs unchangable 
#  * change value without add/remove(size change)
#       thislist[0] = "again" OK 
#       thistuple[0] = "again" # error
# * add/remove 
# thislist.append("AAAA") # changes the size of the list
# thislist.remove(...)
# thislist.insert
# thistuple does has append, insert, remove

## NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

## Tuple Items - Data Types
# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)
# tuple1 = ("abc", 34, True, 40, "male")

## type
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

## The tuple() Constructor
thistuple = tuple(    ("apple", "banana", "cherry")    ) # note the double round-brackets
# create a tuple by coyp another tuple
param =  ("apple", "banana", "cherry")
thistuple = tuple(param)
# thistuple = tuple("apple", "banana", "cherry") # TypeError: tuple expected at most 1 argument, got 3
print(thistuple)

# iterable: list, tuple, set,  get next()
thattuple = tuple([1,2,3,'MN']) # take list as constructor paramter.
print(thattuple)
print(type(thattuple))


thislist = list([1,2,3,'MN'])
thatlist = list((1,2,3,'MN'))

# in case you have tuple, but you need a list, you can convert it list <---> tuple


