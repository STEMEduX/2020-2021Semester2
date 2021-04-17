## Python - Unpack Tuples
## Unpacking a Tuple

# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

## Note: The number of variables must match the number of values in the tuple, if not, you must use an asterix to collect the remaining values as a list.

##Using Asterisk*
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)