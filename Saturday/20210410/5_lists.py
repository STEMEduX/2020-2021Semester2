## Sort
## string
thislist = ["orange", "mango", "kiwi", "pineapple", "basket", "banana", "kiwi" ]
thislist.sort()
print(thislist)

## number
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

## descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

pointA = (0, 0)
pointB = (0, 1)
print(pointA > pointB)
print(pointB > pointA)
## customized sort function
def myfunc(n):
  return abs(n)

thislist = [100, -50, 65, -82, 23]
thislist.sort() # sort by its absolute value
print(thislist)
thislist.sort(key = myfunc)
print(thislist)

def distance(point): # point is a tuple (x, y)
    return point[0]**2 + point[1]**2 ## sqrt(x^2 + y^2) 

thislist = [(0, 0), (0,10), (2, 2)]
thislist.sort()
print(thislist)
thislist.sort(key=distance)
print(thislist)

## case insensitive
## ASCII, compare 2 char, compare ASCII code.
## ASCII, uppercase before lowercase
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
thislist.sort(key = str.lower)
print(thislist)
thislist.sort(key = str.upper)
print(thislist)

## reverse order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
thislist = [2, 1, 8, 9, 7]
thislist.reverse()
print(thislist)