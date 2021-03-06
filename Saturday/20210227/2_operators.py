# Math
# +	Addition	x + y
print(1 + 1)
# -	Subtraction	x - y
print(2 - 1)
# *	Multiplication	x * y
print(2 * 10)
# /	Division	x / y  float division
print(2 / 10) # python do float divid, 0.2 , other language, here you will get 0, integer divide 

# %	Modulus	x % y
print( 7 % 4) # reminder: 3

# ** Exponentiation x ** y
print(2**4) # other language, 2^4

# // Floor division x // y integer division
print(2//10) # 0, this same with other language divide


# Assignment
print('------')
# combination of math with assgin
x = 1
x = x + 1 # x=2
print(x)
x += 1 # x=3
print(x)
# =	x = 5	x = 5
# += x += 3 x = x + 3
# -= x -= 3 x = x - 3
x -= 1
# *= x *= 3 x = x * 3
x *= -1
# /= x /= 3 x = x / 3
x /= 10 # /0
# x /= 0
# %= x %= 3 x = x % 3
x %= 3
# //= x //= 3 x = x // 3
x //= 10
# **= x **= 3 x = x ** 3
x **= 2

# Comparison
# == Equal x == y
x, y = 2, 3
print(x==y) # False 

# != Not equal x != y
print(x!=y) 
# >	Greater than	x > y
print(x > y)
# <	Less than	x < y
print(x < y)
# >= Greater than or equal to x >= y
print(x >=  y)
# <= Less than or equal to x <= y
print(x <= y)

# Logical Operators
# and Returns True if both statements are true	x < 5 and x < 10
# or Returns True if one of the statements is true	x < 5 or x < 4
# not Reverse the result, returns False if the result is true not(x < 5 and x < 10)
print('------')
a, b, c = 0, 1, 2
if a < b and b < c:
    print('True')
if a < b < c:  # easier to read, less typing
    print('OK')

if 1 or 2 or 0:
    print('OK')

x = ''
if not x: # not takes a bool, x will be convert to bool(x) = False 
    print('x is empty')


# Membership
# in Returns True if a sequence with the specified value is present in the object	x in y
# not in Returns True if a sequence with the specified value is not present in the object	x not in y
print('------')
work_days = ["MON", "TUE", "WED"]
if "MON" in work_days:
    print("yes")
else:
    print("no")

if "SUN" in work_days:
    print("yes")
else:
    print("no")

if "SAT" not in work_days:
    print("yes")
else:
    print("no")

# Bitwise
print('------')
# & 	AND	Sets each bit to 1 if both bits are 1
x = 3 # 0011
y = 5 # 0101

z = x & y
# x 0011
# y 0101
# z 0001
print(z)

# homework odd or even
# implement the function
# use bitwise operator: &
# given a integer, 
# if it is odd, return True, otherwise return False
# return i % 2 == 0
# use bitwise operator: &
def is_odd(x: int) -> bool:
    pass

# |	OR	Sets each bit to 1 if one of two bits is 1
w = x | y
# x 0011
# y 0101
# w 0111 # 7
print(w)


# ^	XOR	Sets each bit to 1 if only one of two bits is 1
# 1 ^ 0 = 1
# 0 ^ 1 = 1
# 1 ^ 1 = 0
# 0 ^ 0 = 0
r = x ^ y
# x 0011
# y 0101
# r 0110 # 6
print(r)


# ~ 	NOT	Inverts all the bits
n = ~x
# x 0011, 000000000000011  64bit/ 32bit OS integer: 32bitlong: 00000000..0011
# n 1100 # -4, 8421 = 15, 1111 =15, 1100= 8+4,   16 Hex F = 15 = 1111,  Hex 0-15 , 0000 - 1111
# 1111...11100, first bit indicator sign +/-, first = 1 means negative number, first = 0 position number
print(n)

# google "how negaitve integer store in computer"
# # << Zero fill left shift Shift left by pushing zeros in from the right and let the leftmost bits fall off
# left shift
x << 1
#0011
#0110
# >> Signed right shift Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
# right shift
x >> 1
# 0011 -> 0001

# &= x &= 3 x = x & 3
# |= x |= 3 x = x | 3
# ^= x ^= 3 x = x ^ 3
# >>= x >>= 3 x = x >> 3
# <<= x <<= 3 x = x << 3