## Access Dictionary Items

## You can access the items of a dictionary by referring to its key name, inside square brackets:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x);

## get
x = thisdict.get("model")
print(x)

# print(thisdict["no"]) # not exist, error
print(thisdict.get("no")) # None, this I cannot find it. None

if "no" in thisdict:
    print(thisdict["no"])

if thisdict.get("no") != None:
    print(thisdict["no"])

## Get Keys
x = thisdict.keys() 
print(x) # set 


## Change value
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}


print(car) #before the change
car['year'] = 2000
print(car)

# add a key
car["color"] = "white"

print(car) #after the change

print('-----------')
## Get Values
x = car.values()
# value allow duplicate, 
print(x) # values: list?* not set? tuple?

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


## Add a new item to the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change


print('---------')
car1 = {"name": "toyota", "year": 2000}
car2 = {"name": "ford"}
cars = [ car1, car2]
# carset = {car1, car2} # TypeError: unhashable type: 'dict'
# hash, conver data/type  -> hash value?
# hash value -> number, orderable/sort.  number -> sort from min -> max, low -> high.
# people? sort people age/number, weight, height, 
# string ascii code, sort 
# hash function,  input data: car, people, hash algorithm/encode/address memory -> hash value 

# hashtable/set/hashmap/dict
[1,5,6,8]
# array
# 0 -> 1, 1 -> 5, ....  get element at position 1000, O(1) time, 
# 0 32bit, 1 32 bit.. 32*999. -> postition 1000 , 100000  -> O(1)
# 0 16bit, 2 8 bit, 3 4it -> 1000, size (1...999) positon  -> O(999), 100000, O(99999), O(N) give result
# Array access by index take O(1)
# dict access by key take O(1)

# hash value, 
# [key hash values ] -> array
# hash value of key -> postion find value
# key -> hash value -> table -> position, o(1)

print(type(cars))
print(type(cars[0]))