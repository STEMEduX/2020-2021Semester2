# List Comprehension
## Filter
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)
# a list of fruits which len == 5
newlist = []
for x in fruits: # start from the first element, next(), next() is None
  if len(x) == 5:
    newlist.append(x)

## for iterable
# while x.next() != None:
#     # do somthing here

print(newlist)

## use comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
newlist = [ 'name:' + x for x in fruits if len(x) == 5]
print(newlist)

## Iteratable: list, set, tuple, dictionary.keys()
## interface/pattern,  next() [1, 2, 3] -> None/null
## The Syntax
## newlist = [expression for item in iterable if condition == True]
## filter, select elements by condition, change type
newlist = [x for x in fruits if x != "apple"]
## create list
newlist = [x for x in range(10)]
print(newlist)
# [0, 1, .. 9]
## transform, for each element, do some calculation/conversion/even to another type
newlist = [x.upper() for x in fruits]
print(newlist)
newlist = [ len(x) for x in fruits]
print(newlist)
newlist = [ (x, len(x)) for x in fruits]
print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# x if condition else other value
# if x meet the condition, return x, otherwise return new value

# fruits is a list

for x in fruits: # take every element in list/fruits, put it into varible: x
    print(x) # process x here

for i in fruits:
    print(i) # print(x)

# https://en.wikipedia.org/wiki/Elvis_operator
## javascript/c#/java:
# c = a>b ? a: b  // if (a>b) is true, c=a, otherwise c =b 
# c = max(a, b)
# python
a = 10
b = 100
c = a if a>b else b # if (a>b) is true, c=a, otherwise c =b 
print(c)
c = max(a, b)
print(c)