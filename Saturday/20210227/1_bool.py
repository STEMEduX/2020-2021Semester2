# Boolean Values
## True / False
True
False
# if a == true:
#     pass

print(10 > 9)

print(10 == 9)

print(10 < 9)

## in if
if 10 > 9:
    print("correct")
else:
    print("wrong")

# Evaluate Values and Variables
## bool("helo")
## bool(18)
## bool(["apple", "cherry", "banana"])
print('-------')
print(bool("hello")) # if string not None or empty, True, otherwise: False
print(bool(''))
google_response = ""
if bool(google_response):
    print("not empty")
else:
    print("empty")

print('-------')
print(bool(12))
print(bool(-1000))
print(bool(0))

print('-------')
print(bool([])) # False, it is empty
print(bool( [ 1, "None"]) )
print(bool(None))
print(bool([None])) # True: cause take a non empty list

print('-------')
print(bool(False))
# bool(None)
# bool(0)
# bool("")
print('-------')
print(bool(())) # () empty: tuple, () empty tuple (x, y) tuple, (x, y, z) tuple,  
print(bool((2))) 
print(bool((0,0))) # not empty tuple: True

# bool([])
print('-------')
print(bool({})) # False: empty dictionary
print(bool({"firstName": "Jen", 5: 25 }))
print({"firstName": "Jen", 5: 25 })


# 

# Functions can Return a Boolean
print('-------')
x = 200
print(isinstance(x, int))
print(isinstance(x, str))
print(isinstance(str(x), str)) # True: type of str(x) is str