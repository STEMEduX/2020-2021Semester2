1  # Name Convention
# alpha, number, _,
# _how_are_you
# hw
# 9chars invalid
# i, j  # i is ...

# Camel Case
# first letter is lower case, each word starts uppercase
# standard in javascript, nodejs, typescript,
# Python also use it
footballScore = 0
dayOfMonth = 1

# Pascal Case
# first letter is uppcase case, each word starts uppercase
# C#, C++, VB, Basic
FootballScore = 0
DayOfMonth = 2

# Snake Case
# all letters are lowercase, use _ connect words
# recommended by Python
football_score = 1
day_of_month = 3

# Assign Mulitple Variables
num1, num2 = 1, 2
print(num1, num2)

# swap
a, b = 1, 2
a, b = b, a  # a, b = temprory place,
# tuple, (key, value) 2 related data, (k1, k2, k3 ...)
# (b, a) => (a, b)
# temp = a
# a = b
# b = temp
print(a, b)  # 2, 1

# Unpack a collection
listA = ["One", "Two", "Three", "Four"]
# n1 = listA[0]
# n2 = listA[3] # Three
print(listA[2])  # Three

n1, n2, n3, n4 = listA
print(n1, n2, n3, n4)

nn1, nn2, *remain = listA
print(nn1, nn2, remain)

*allExceptLast, lastN = listA
print(lastN, allExceptLast)

# print second element of listA
# _ mean 1 variable name I do not care, and I will not use it later
# * mean multiple elements,
print(listA[1])
_, second, *_ = listA
print(second)

listB = [1, 2]  # []
_, _, *remain = listB
print(remain)

print('--------------')
listC = [1, 2, 3, 4]
_, *L2, _ = listC
print(L2)

listC = [1, 2, 3, 4, 5]
_, *L2, _ = listC
print(L2)  # 2, 3, 4

# Global Variables

print('------------------')
g = "global"  # g1


def get_min_value(a, b):
    g = "local"  # g2
    print(g)  # g2 the closest is on on line 81
    return min(a, b)


def get_again():
    # global g # optional in this function
    print(g)  # g on line 79 is closest and this function can see


get_min_value(1, 2)
get_again()
print(g)  # g1

print('----------------')
name = "global_name"


def change_name():
    name = "new name"  # this is a new local variable declaration.


def change_name_gain():
    global name
    name = "new again name"


change_name()
print(name)  # did change_name success ? not working here

change_name_gain()
print(name)
