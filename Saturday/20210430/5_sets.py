## Loop Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

## Common mistake: RuntimeError: Set changed size during iteration
thisset = {"apple", "banana", "cherry"}
for x in thisset: # keep collection unchanged in size
  thisset.add(x + 'a') # or thisset.remove(x)
  print(x)
