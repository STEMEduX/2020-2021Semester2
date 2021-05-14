## Access Dictionary Items

## You can access the items of a dictionary by referring to its key name, inside square brackets:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]

## get
# x = thisdict.get("model")

## Get Keys
# x = thisdict.keys()

## Change value
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# print(x) #after the change

## Get Values
x = thisdict.values()

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change


## Add a new item to the original dictionary, and see that the values list gets updated as well:

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["color"] = "red"

# print(x) #after the change