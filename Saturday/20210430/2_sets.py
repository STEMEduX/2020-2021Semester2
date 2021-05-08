## Access Items
## list, set, tuple
## traversal, iteration,
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


## Check exists
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

## index is not supported
## subscript mean index
# print(thisset[1])

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.
thisset = {"apple", "banana", "cherry"}
thisset.add("apple2")
print(thisset)
thisset.remove("apple")
print(thisset)

# change apple to apple2
# add apple2, remove apple
