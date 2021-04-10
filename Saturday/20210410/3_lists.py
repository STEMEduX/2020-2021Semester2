# Traversal List

## For, for each element, do something
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
print(thislist)

## By Index
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)): # range(4) [0,1,2,3] left close, right open
  print(thislist[i])
# range(3) => 0, 1, 2

## While
print('while -------------')
thislist = ["apple", "banana", "cherry"]
i = 0 # initialization
while i < len(thislist): # terminate condition
  print(thislist[i])
  i = i + 1 # increase i 
# ctrl + c, break key, it will terminate you current running command

# List Comprehension
print('----------')
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]