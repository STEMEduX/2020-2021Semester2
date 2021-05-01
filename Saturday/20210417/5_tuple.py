## Loop Through a Tuple
## for
thistuple = ("apple", "banana", "cherry")
for x in thistuple[1:]: # loop start from "banana"
  print(x)

print('-----------')
## length
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

## Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0 # initalize
while i < len(thistuple): # check if reach the end
  print(thistuple[i])
  i = i + 1 # increase the i