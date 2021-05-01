## Remove Set Items
## Remove Item
# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)

# If the item to remove does not exist, remove() will raise an error.
# thisset.remove("not here") # KeyError

# If the item to remove does not exist, discard() will NOT raise an error.
# thisset = {"apple", "banana", "cherry"}
# thisset.discard("banana")
# print(thisset)
# thisset.discard("not here")
# print(thisset)


## pop() remove last one
## The return value of the pop() method is the removed item.
# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset)

## pop a empty set will error out
# thisset = {}
# thisset.pop() # error

## The clear() method empties the set:

# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)

## The del keyword will delete the set completely:

# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset) # NameError: name 'thisset' is not defined