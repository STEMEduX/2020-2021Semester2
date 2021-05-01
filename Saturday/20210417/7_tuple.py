## Other methods
fruits = ("good", "apple", "banana", "cherry", "apple", "other", "apple")
print(fruits.count("apple"))
print(fruits.index("apple"))

# print(fruits.index("bananaA")) ## error, dead here
if "bananaA" in fruits:
    print(fruits.index("bananaA"))
print("do some job")
## https://www.w3schools.com/python/python_tuples_exercises.asp