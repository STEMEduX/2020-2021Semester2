## Add Set Items
## Item
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

## Another Set, merge
# Add elements from tropical and thisset into newset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "apple"}
thisset.update(tropical)
print(thisset)

## Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

mytuple = (1, 2, 'apple')
thisset.update(mytuple)
print(thisset)

## update
# def update(s, i): # i is a iterable
#     for e in i:
#         s.add(e)

thisset = { 'apple', 1}
thisset.add('apple')
print(thisset)
