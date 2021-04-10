## Tuple
## Tuples are used to store multiple items in a single variable.
## Tuple is one of 4 built-in data types in Python used to store 
## collections of data, the other 3 are List, Set, and Dictionary, 
## all with different qualities and usage.
## A tuple is a collection which is ordered and unchangeable.
## Tuples are written with round brackets.

## Tuple items are ordered, unchangeable, and allow duplicate values.
# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)
# print(thistuple[0], "---", thistuple[2])
# thistuple[0] = "again" # error

## length
# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))

## Tuple With One Item
# thistuple = ("apple",)
# print(type(thistuple))

## NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

## Tuple Items - Data Types
# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)
# tuple1 = ("abc", 34, True, 40, "male")

## type
# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))

## The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

thattuple = tuple([1,2,3,'MN'])
print(thattuple)
print(type(thattuple))
