## Remove Set Items
## Remove Item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# If the item to remove does not exist, remove() will raise an error.
# thisset.remove("not here") # KeyError

if "not here" in thisset:
    thisset.remove("not here")

thislist = [ "apple", "banana", "apple"]
thislist.remove("apple")
print(thislist)


# If the item to remove does not exist, discard() will NOT raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
thisset.discard("not here") # no error
print(thisset)


print('------------')
## pop() remove last one
## The return value of the pop() method is the removed item.
thisset = {"banana", "apple", "cherry"}
# thisset[0] # order is not predictable. hashing, easy to find
x = thisset.pop() # banana - last element
print(x)
print(thisset)

print('------------')
thislist = ["apple", "banana", "cherry"]
x = thislist.pop() # cherry 
print(x)
print(thislist)

## pop a empty set will error out
thisset = {}
if thisset:
    thisset.pop() # error

# thislist = []
# thislist.pop()

# check collection empty:
# use if

## The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
if not thisset:
    print("empty")

## The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) # NameError: name 'thisset' is not defined