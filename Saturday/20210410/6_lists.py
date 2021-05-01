## Copy 

thislist = ["apple", "banana", "cherry"]
mylist = thislist
thislist.append("new")
mylist.append("new2")
print(thislist) # ['apple', 'banana', 'cherry', 'new', 'new2' ??? ]
print(mylist)

## by reference
# thislist ----> ["apple", "banana", "cherry"]
# mylist ----> thislist ----> ["apple", "banana", "cherry"]
# mylist ----> * thislist ----> ["apple", "banana", "cherry", "new"]
# * mylist ----> thislist ----> ["apple", "banana", "cherry", "new", "new2"]
# mylist ----> (print) thislist ----> ["apple", "banana", "cherry", "new", "new2"]
# (print) mylist ----> thislist ----> ["apple", "banana", "cherry", "new", "new2"]
# thislist -> [] <- mylist

## by value
this_int = 3
my_int = this_int # copy this_int -> 3, my_int-> 3
print(this_int, my_int) # 3, 3
my_int = 100
print(this_int, my_int) # 3, 3 vs 3, 100

## efficiency or performance
# for collections by reference, most popular/moden languages, except C++ has different pattern

print('----------')
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() # thislist -> [*] , mylist-> [**]
thislist.append("new") # thislist -> [*,"new"]
mylist.append("new2") # mylist -> [**, "new2"]
print(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist) # construct/create another list by passing thislist as parameter
thislist.append("new")
mylist.append("new2")
print(thislist)
print(mylist)

# comment highlight code, use key: Ctrl + /, CMD + /
#asdfkjaskj

"""
this is a comment
this is line 2
"""