# Assign String to a Variable
a = "Hello"
print(a)

a = 'hellow, how'
print(a)
print('------')

# Multiline Strings
m1 = '''
this is 
multiline
'''
print(m1)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays
# index access string, index 0 based
a = "Hello, World!"
# letter - index
# H - 0
# e - 1
print(a[1])

print('------')
# Looping Through a String
for x in "banana":
  print(x)

# String Length
# len(s) --> js, string.length
a = "Hello, World!"
print(len(a))

# Check String (in aka substring)
txt = "The best things in life are free!"
print("free" in txt) # bool: true/false

# "free" in txt is a function, you can use it in if statement 

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")

# Slicing
b = "Hello, World!"
# b[2:5] take sub string from index 2 to 5
#Hello, World!
#0123456789abcd
#  llo,     will the result also take ,
print(b[2:5]) # [left, right)

# Slice From the Start
h = b[0:5]
print(h)
h = b[:5]
print(h)
print(b[0:5] == b[:5])

# Slice To the End
w = b[7:13]
print(w)
w = b[7:]
print(w)
print(b[7:100]) # will it error out? or ** it will print World!, python is smart!

# # Negative Indexing
print('----------')
# "Hello,"
b = "Hello, World!"
#    012[3       -3 -2 -1
print(b[3:-3]) # lo, Wor
print(b[-1])

# string can be treat as list of chars
print('----------')
nums = [1, 2, 3, 4, 5, 6]
print(nums[-1])
print(nums[5])
print(nums[2:5])

# # Uppercase
print(b.upper())
c = "hello23%^&*"
print(c.upper())

# # Lowercase
print(b.lower())
print(c.lower())

a = "abc"
b = "abe"
c = "Abc"
d = "abc"
print(a > b) # ... False
print(a > c) # ... ? True
print(a == d)

c= "Hello, world"
d= "hello, world"
# true
print(c.lower() == d.lower())

if c.upper() == d.upper():
  print('same')
else:
  print('diff')

# C#, Java, Python ...
# string is call immutable
# immutable, once created, it cannot be changed.
a = "123"
a = "345"
# a is box with label name "a", we put string "123" into the box
# "345" -> box name "a"
# content in the box change. but not "123" string itself
# a -> memA [] -> ["123"]
#      memA [] -> ["345"]   ["123"]
# d[0] = d[0].upper() # this will error out
# print(d)
print('----------')

a = "hello, world";
print(a.capitalize())
o = a.capitalize()
print('a=', a)
print('o=', o)
print('----------')
b = a[0] + a[1].upper() + a[2:] # 'llo ...'
print(b)


# http://www.asciitable.com/
#10 base: 0 - 9, 10 , 11 ...
# 16 base: 0 - 9, a, b, c, d, e, f, 10, 11 ...19, 1a, 1b ... 
# 8 base: 0 - 7, 10, 11.. 17, 20... 

# # Remove white space: strip
res = " I am a boy     "
print("|" + res.strip() + "|")
print("|" + res + "|")

# # Replace String
s = "I have 1 apple"
replaced = s.replace("1", "one")
print("replaced=", replaced)
print("origin=", s)
print('--------')
s= "I have 111 apple"
replaced = s.replace("1", "one")
print("replaced=", replaced)
print("origin=", s)

# # Split String
s = "I have a dog"
splitted = s.split(' ')
print('splitted=', splitted)
splitted = s.split('a')
print('splitted=', splitted)
print("origin=", s)


# # String Concatenation
print("how are" + " you?" + '''good,
what is
 this
''')

# # String Format, position based
age = 36
txt = "My name is John, and I am {} years old"
print(txt.format(age))

name = "Jen"
txt = "My name is {}, and I am {} years old"
print(txt.format(name, age))
print(txt.format(age, name))

# string interpolation, string template (JavaScript)
txt = f"My name is {name}, and I am {age} years old"
print(txt)
# Javascript do the following
# txt = `My name is ${name}, and I am ${age} years old`


# # Escape Character
# # List here:
# # https://www.w3schools.com/python/python_strings_escape.asp
"\r\n" "\n\r"


# # Other string methods
# # https://www.w3schools.com/python/python_strings_methods.asp



s = "I have a white dog"
ss = s.split(' ')
print(ss) # list of string
print(ss[:2])
