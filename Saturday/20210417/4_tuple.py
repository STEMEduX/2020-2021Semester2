## Python - Unpack Tuples
## Unpacking a Tuple

student = (12, "james", "bond", 8, 4.5, "5850 Opus pkwy") # hundred element,
print("name:" + student[1] + ", " + student[2])
(no, firstname, lastname, grade, gpa, address) = student
print("name:" + firstname + ", " + lastname)

## Note: The number of variables must match the number of values in the tuple, if not, you must use an asterix to collect the remaining values as a list.

##Using Asterisk*
(no, firstname, lastname, *remain) = student
print("name:" + firstname + ", " + lastname) # 1 parameter
print("name:", firstname, lastname) # 3 parameter
print(no)

# print("remain" + remain) 
'''
why ? "remain" is a string, remain is list, 
+ operator, for string, it concat 2 string together.
but python get a string and list, so it does not know what to do
'''
print("remain" + str(remain))
print("remain", remain)  # passing 2 params to print function

# _ can be used as place holder
(_, firstname, lastname, *_) = student
print(firstname, lastname)

print('-------------')
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

(green, *_, red) = fruits

print('-------------')
student = (12, "james", "bond", 8, 4.5, "5850 Opus pkwy") # hundred element,
(no, _, _, grade, *_) = student # will this work? can only use 1 *
(no, *_, grade, _, _) = student # will this work? can only use 1 *

print(no, grade) 