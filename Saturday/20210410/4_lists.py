# List Comprehension
## Filter
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

## use comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)

## The Syntax
## newlist = [expression for item in iterable if condition == True]
## filter
# newlist = [x for x in fruits if x != "apple"]
## create list
# newlist = [x for x in range(10)]
## transform
# newlist = [x.upper() for x in fruits]
# newlist = [x if x != "banana" else "orange" for x in fruits]