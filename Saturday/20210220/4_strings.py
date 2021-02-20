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

# # Uppercase

# # Lowercase

# # Remove white space: strip

# # Replace String

# # Split String

# # String Concatenation

# # String Format, position based
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

# # Escape Character
# # List here:
# # https://www.w3schools.com/python/python_strings_escape.asp

# # Other string methods
# # https://www.w3schools.com/python/python_strings_methods.asp

