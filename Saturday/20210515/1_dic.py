## Dictionary

## Dictionaries are used to store data values in key:value pairs.
## A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# List, Set, Tuple, Dict, 
# HashMap, key -> value
# word, key -> meaning of the word, value.
# lookup dictionary by key/word
# lookup value using key. 
# like access value using index in array. 
# array, dict
# array -> index, value , index has to be number/integer, 1 index for each number. 
# [0, 1, 2, 3, 4, 5] ["one", _, "two", _, _, "five"] , you need a array with size 6, 
# there are space are empty
# dic -> key, value, key type: string, number, key has to be unique
# {1: "one", 2: "two", 5: "five"}
# array, 2M of size, most of it 0, 5 elements have value
# array[2M], [0..                      2M-1] memory. 32bit number, each number take 4bits. cosume 8Mb m
# { pos1: value1, pos2: value2 ... pos5: value 5} (32bit + 32bit) * 5 = 40b 
 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

empty_dict = {}
print(empty_dict)
print(type(empty_dict))

# empty_set = {} # this a dic
empty_set = set()
print(type(empty_set))

## Dictionary Items
## Dictionary items are ordered, changeable, and does not allow duplicates.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
print(thisdict["year"])

## Ordered or Unordered?
## As of Python version 3.7, dictionaries are ordered. 
# In Python 3.6 and earlier, dictionaries are unordered.
# { 1: "one", 3: "three", 2: "two"} unorder
# { 1: "one", 2: "two", 3: "three"} order

## Changeable
## Dictionaries are changeable, meaning that we can change, 
## add or remove items after the dictionary has been created.


## Duplicates Not Allowed, key cannot be duplicate,
## value

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

thisboy = {
  "yearofbirth": 2000,
  "favornumber": 2000
}
print(thisboy)
