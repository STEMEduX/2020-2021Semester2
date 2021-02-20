# js: number, string, function, object, null, undefined, array, boolean
# Bultin DataTypes
# Text Type:	str
# Numeric Types:	int, float, complex = 4 + 5i
# collections
    # Sequence Types:	list, tuple, range
    # Mapping Type:	dict 
        # key -> value
    # Set Types:	set, frozenset
        # set, list allow duplcate values, set does not
# Boolean Type:	bool
    # true/ false
# Binary Types:	bytes, bytearray, memoryview
    # binary: bit 0/1, 01, 1110, 1110010111110000

# Type function
x = 5
print(type(x))

y = "how are you?"
print(type(y))

c = complex(5, 8)
print(type(c))

d = 5 + 8j
print(type(d))
# Type Inference
# s = "aaaa"
# b = s // 3
# print(b)

# Numbers
# int
# float
# complex


x = 1.10
y = 1
z = 3+5j

print(type(x))
print(type(y))
print(type(z))

print('-------')
# float, assgin its value to 10
xy = 10.0
print(type(xy)) # modify line 49, and I want float as the type.

# Random Number
import random

print(random.randrange(1, 10)) # 1 to 9, min=1, max=10-1, [0, 100)
print(random.randrange(1, 10))
print(random.randrange(1, 10))
print(random.randrange(1, 10))
