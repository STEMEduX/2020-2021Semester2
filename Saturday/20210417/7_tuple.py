## Other methods
fruits = ("good", "apple", "banana", "cherry", "apple", "other", "apple")
print(fruits.count("apple"))
print(fruits.index("apple"))

# print(fruits.index("bananaA")) ## error, dead here
if "bananaA" in fruits:
    print(fruits.index("bananaA"))
print("do some job")
## https://www.w3schools.com/python/python_tuples_exercises.asp

# What is the difference between fruits={"a","b"} and fruits=("a","b")
print('------------')
#initalizer, declare a variable and assign value to it.
fruits={"a","b"} # set, initialize a set
print(type(fruits))
fruits=("a","b") # tuple
print(type(fruits))
fruits=["a","b"] # list
print(type(fruits))


